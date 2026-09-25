---
layout: post
title: "Command Line-ception"
subtitle: "a CLI wrapper to a CLI"
date: 2024-12-18
background: '/img/posts/2024-12-18-cli-ception.jpg'
---
## *sorry there's no jump to recipe button, the context is a bit important*

This latest project happened a bit unexpectedly. I was finishing up our shop's deployment of the PowerShell DSC for ArcGIS and was excited to set up the disaster recovery parameters handled by the WebGIS DR tool. The WebGIS DR tool is a command line interface (CLI) that has been packaged with ArcGIS Enterprise (colloquially known as Portal) since at least the 10.5 version. This takes a backup of the ArcGIS Enterprise in a variety of styles: `backup`, `full`, and `incremental`.

But this begs the question, if the purpose of a disaster recovery tool is to revert to a state of normalcy from some *unexpected* disaster, then should our disaster recovery be automated? The answer is yes. And you could easily set this as an automation with a simple `.bat` file if you only wanted to have a single type of backup. You'd write something like this, assuming you're not wanting to put in additional files inside of the ArcGIS Enterprise installation paths:

```cmd
cd "C:\Program Files\ArcGIS\Portal\tools\webgisdr"
webgisdr --export --file webgisdr.properties
```

It's simple. Which is really part of the problem. There is not a flag for the kind of backup you want to run. That information is stored on `line 28` of the `webgisdr.properties` files, in a parameter that looks like this:

```
# Specify the Web GIS backup restore mode: backup, full or incremental. Default is backup.
BACKUP_RESTORE_MODE = BACKUP
```

And if you're not really steeped in backup modes, you might be wondering why there are three kinds, and maybe why you'd want each one. 

- **Backup** - This is the WebGIS DR tool's default setting. It is a regular copy. The same kind of copy/paste type deal everyone is duly familiar with.

- **Full** - This is the same as a backup. However, this also allows you to access the third type of backup, incremental.

- **Incremental** - This is a backup that can be used only after saving a full backup. It only captures data from after the full backup. The advantage is this file is smaller, and runs faster than either the backup or full modes.

If you're looking for speed of backups and want also to minimize storage size of your backups, then you'll want to pursue a strategy utilizing full and incremental backups in tandem. Assuming for a moment that you didn't care to run default backup, you'd really need to hold onto two copies of the webgisdr.properties file and maybe name them with suffixes like `_full` and `_incremental`. 

Now your simple `.bat` file is two simple `.bat` files that each reference a separate `.properties` file so that you can set a single parameter differently. 

```
#maybe this runs every 12 hours
cd "C:\Program Files\ArcGIS\Portal\tools\webgisdr"
webgisdr --export --file webgisdr_incremental.properties
```
```
#maybe this runs every 7 days
cd "C:\Program Files\ArcGIS\Portal\tools\webgisdr"
webgisdr --export --file webgisdr_full.properties
```

And on top that, you still need to prune your old backup copies. Unless storage space isn't a concern for your organization. Which would be a cool non-problem to have.

## Two Levels
This is where I had a moment of clarity. What I really wanted.

[!["a still from the movie inception, texas has been added to say, a command line within a commandline. two levels."](/img/posts//img/posts/2024-12-18-cli-ception.jpg)](/img/posts//img/posts/2024-12-18-cli-ception.jpg)

And it wasn't 6 files (3 `.bat` files and their 3 corresponding `.properties` files). 

It was a single file that I could schedule and then never worry about disaster recovery again... ...you know, except if disaster were to strike... ...and obviously a bi-annual disaster recovery exercise because you don't want your first time testing your disaster recovery option to be when you actually have to use it to continue business operations.

I needed something like, a command line interface. Where I could state an option within the scheduled task and call it a day.

It ended up looking like this:

```
#on a weekly task
WebGISDR-cli-wrapper.py -full 4
```
```
#on a daily task
WebGISDR-cli-wrapper.py -incremental 4
```

With these extra options, I set the type of backup and the number of copies to retain as well.

And if you're like me, the question you're probably asking is, but how? And fortunately, that's pretty easy to answer. I wrote a CLI wrapper in Python in about a hundred lines that really boils down to 3 functions:

1. `prune_copies()` - take a directory, search for the `.webgissite` files that match the selected backup mode, and keep only the number that you want to have on hand at a given time. This results in dropping a file every time before you run the WebGIS DR tool again. 
2. `set_WebGISDR()` - open the `webgis.properties` file, change the parameter `BACKUP_RESTORE_MODE` parameter to match the user input
3. `run_WebGISDR()` - runs the original WebGIS DR CLI like it would normally run: `webgisdr --export --file webgisdr.properties`

We'll go ahead and look at it in a logical sequence:

This is the flow of the CLI. We take some arguments, feed those to our main function, and then distribute those to the three primary functions as needed.

```python
def main(backup_arguments: argparse.Namespace):
    print(
        f"\tbackup_mode is: {backup_arguments.mode}\n\tcopies to retain: {backup_arguments.copies}\n"
    )
    prune_copies(WebGISDR_backups_path, backup_arguments)
    set_WebGISDR(WebGISDR_dir, WebGISDR_filename, backup_arguments.mode)
    run_WebGISDR(WebGISDR_dir, WebGISDR_filename)


if __name__ == "__main__":
    arguments = configure()
    main(arguments)
```

For us to ask our user to input options at runtime, we have to do some prep-work in this configure function. This was my first time using the argparse library and it was fairly painless. Looking forward to doing more with it if I need to set runtime arguments again. There's really not a reason to ask for more from the user other than what kind of backup or the number of copies that they want to retain. There are definitely more complicated backup copy management strategies but for 80% of use-cases this is likely satisfactory.

```python
def configure():
    """Configures the user input arguments

    Returns:
        argparse.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        choices=["FULL", "INCREMENTAL", "BACKUP"],
        type=str.upper,
        help="""the type of WebGISDR backup to be performed: backup, full, or
        incremental. this input is case insensitive.
        """,
    )
    parser.add_argument(
        "copies",
        choices=range(1, 8),
        type=int,
        help="""
        the number of copies to retain. this is the number of backups
        only for the backup mode input/selected. this is exclusive of the primary backup
        which will run at the end of the script.
        """,
    )
    print(f"{spacer}\n{spacer}\nRunning WebGISDR Automation")
    return parser.parse_args()
```

And for a bit of context, here's what that would look like if you ran the --help flag.

*the WebGISDR Automation CLI Wrapper's help menu*
```
Running WebGISDR Automation
usage: WebGISDR-cli-wrapper.py [-h] {FULL,INCREMENTAL,BACKUP} {1,2,3,4,5,6,7}

positional arguments:
  {FULL,INCREMENTAL,BACKUP}
                        the type of WebGISDR backup to be performed: backup, full, or incremental. this input is case insensitive.
  {1,2,3,4,5,6,7}       the number of copies to retain. this is the number of backups only for the backup mode input/selected. this is exclusive of the        
                        primary backup which will run at the end of the script.

options:
  -h, --help            show this help message and exit
```

Moving on, we can look at the imports and constant variables. For most use-cases, the only thing that should need to be filled out is the `WebGISDR_backups_path` variable. Which, should live in a machine that isn't the Portal component. Because. Disaster.

You'll also notice that the import statements are fairly light. This is designed to utilize components of the standard library in Python so that a minimal environment can be set up on the Portal machine. Also `pathlib` is just an elegant library. When I first learned Python all the file management stuff was handled using the `os` library, I've found that `pathlib` much easier to handle and it is more readable as well.

*import statements and constant variables*
```python
import argparse
import os
import subprocess
from pathlib import Path

# Variables
WebGISDR_filename = "webgisdr"
WebGISDR_dir = Path(r"C:\Program Files\ArcGIS\Portal\tools\webgisdr")
WebGISDR_backups_path = Path(r"\\some-filepath-here")
spacer = "-" * 50
```

Finally we're at the primary three functions. Here's `prune_copies()`. 

- We create a list of paths from the directory indicated by the constant `WebGISDR_backups_path`, where the backup matches our user input (using dot notation from our argument names that we defined in the configure function). All backup copies look like: `yyyymmdd-hhmmss-TYPE.webgissite` with this in mind, we can run a wildcard (*) string search to grab anything that matches our `TYPE`
- Sort the list in descending order, this means that oldest copies are at the end
- Create another list through a list comprehension so that we can have a pretty output that only includes file names
- Create a list of backups to be retained by slicing the sorted list according to our user input
- Create a list of backups to be pruned by slicing from the other direction
- Iterate through our prune list and use `pathlib`'s `.unlink()` to remove those from the file system

```python
def prune_copies(webgisdr_backups_path: Path, backup_arguments: argparse.Namespace):
    """Prunes a list of files according to the number of copies.

    Args:
        webgisdr_backups_path (Path): a directory path to the .webgissite backups
        backup_arguments (argparse.Namespace): the user input arguments for backup and copies
    """
    print(f"Pruning backups")
    WebGISDR_backups = list(
        webgisdr_backups_path.glob(f"*{backup_arguments.mode}.webgissite")
    )
    WebGISDR_backups.sort(reverse=True)
    file_names = [file.name for file in WebGISDR_backups]
    backups_retained = file_names[: backup_arguments.copies]
    backups_pruned = file_names[backup_arguments.copies :]
    for file in backups_pruned:
        Path(webgisdr_backups_path, file).unlink()
    print(f"\tretained:\t{backups_retained}\n\tpruned:\t\t{backups_pruned}\n")
    return
```

Next we're setting the parameter of the `webgisdr.properties` file to match the user input type in the appropriately named `set_WebGISDR()` function.

- We create a `Path` to the file
- Read in the file as a `string`
- Create a list of strings where each item is a new line
- Iterate through the lines and find the line with the parameter `BACKUP_RESTORE_MODE`. Replace this list item with a string that utilizes our user input
- Write the list of strings as string using a new line joiner

```python
def set_WebGISDR(webgisdr_dir: Path, webgisdr_filename: str, backup_mode: str):
    """Sets the WebGISDR configuration file's BACKUP_RESTORE_MODE property

    Args:
        webgisdr_dir (Path): the webgisdr tools directory path on the arcgisportal machine
        webgisdr_filename (str): the name of your webgisdr configuration file, it is normally 'webgisdr'
        backup_mode (str): the backup mode that was input as an argument
    """
    print(f"Setting {webgisdr_filename}.properties: BACKUP_RESTORE_MODE")
    WebGISDR_properties = Path(webgisdr_dir, f"{webgisdr_filename}.properties")
    file_content = WebGISDR_properties.read_text()
    lines = file_content.splitlines()
    for i, line in enumerate(lines):
        if "BACKUP_RESTORE_MODE =" in line:
            print(f"\tcurrent value:\t{line.split(' = ')[-1]}")
            lines[i] = f"BACKUP_RESTORE_MODE = {backup_mode}"
    WebGISDR_properties.write_text("\n".join(lines
```

Lastly, we just need to run the standard WebGIS DR tool in the function `run_WebGISDR()`.

- Change directory to the WebGISDR tool within the Portal installation
- Craft a string that will be used in the `subprocess.run()` function, this is analagous to opening a command prompt terminal
- Run the `webgisdr` command

*Python code describing the `run_WebGISDR()` function:*
```python
def run_WebGISDR(webgisdr_dir: Path, webgisdr_filename: str):
    """Runs the WebGISDR command-line utility

    Args:
        webgisdr_dir (Path): the webgisdr tools directory path on the arcgisportal machine
        webgisdr_filename (str): the name of your webgisdr configuration file, it is normally 'webgisdr'
    """
    print(
        f"Changing Directory to {webgisdr_dir}\n\trunning standard WebGISDR utility now\n\n{spacer}\n{spacer}"
    )
    os.chdir(webgisdr_dir)
    cmd_webgisdr = f"webgisdr --export --file {webgisdr_filename}.properties"
    subprocess.run(cmd_webgisdr, shell=True)
    print(f"{spacer}\n{spacer}\nAll Operations Complete\n{spacer}\n{spacer}")
    return
```

And that's it. A fairly painless automation for setting and forgetting an out-of-the-box disaster recovery solution. When it runs it looks like this:

[!["A terminal output from the running of the WebGISDR CLI wrapper"](/img/posts/2024-12-18-cmd-snippet-02.png)](/img/posts/2024-12-18-cmd-snippet-02.png)
*terminal output when run*

If you'd like to use it in your own deployment you can find it on my GitHub here:
[https://github.com/FeralCatColonist/Spatial-Grimoire/blob/main/WebGISDR-cli-wrapper.py](https://github.com/FeralCatColonist/Spatial-Grimoire/blob/main/WebGISDR-cli-wrapper.py)