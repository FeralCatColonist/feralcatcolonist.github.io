---
title: "[R] You Ready, Kids?"
description: "Who lives in a [kernel] [within] the [ArcGIS Pro Notebook]?"
date: "2026-10-07"
image: "/img/posts/2026-10-07-r-you-ready-kids.jpg"
categories: ["ArcGIS", "R", "Conda"]
aliases: ["/2026/10/07/r-you-ready-kids.html"]
---
I try not to be a competitive person. Most of the time I'm fairly successful, I can focus on me and let other things lie. Unfortunately, there are a few situations that tend to goad me into action; creating, what some might term, a, *hold my krabby patty* moment.

Mostly these are some flavor of:

> `item/action/technique` doesn't work in `<insert thing here>`\
> I don't believe that anyone can actually `<insert thing here>`

A few weeks ago, I was whisked down into the depths of single combat. With no one actually, except the shade of some gatekeeper, probably more like Dark Link in Ocarina of Time. In the GIS Discord, it started with a stray comment:

> "I found a non-esri result, but it bluntly told me that you can't do `R` in arcgis notebooks"
> 
> *-Garbage Panda Trifecta*

My immediate response was:

> Who wants to use a filthy ArcGIS notebook anyway?\
> Literally the worst way to jupyter

To be fair, the Esri devs are doing the Lord's work by exposing users to Python programming outside of a terminal within the GUI. The inverse is every SaaS that launches their own [shitty bespoke language that provides zero value outside of their own environment^tm^]{.smallcaps}.

Everyone's got to start somewhere. I started somewhere.\
Anyway, as petty as my comment was, I was already hooked.

## absorbent and yellow and porous is he!

I turned it over and over in my mind's eye.\
*squints* \
I doubt it's impossible.\
*squints harder*\
I have a Mendela Effect memory of an ArcGIS Notebook having a kernel switch button for R.\
*do I actually have a Mendela Effect memory?*\
I am 100% sure it was the Bearenstein Bears.\
*why do I think its the Mandala Effect?*\
Let me just browse the docs. And Wikipedia.\
*begins browsing squintingly*

![](/img/posts/2026-10-07-346-minutes-later.webp){fig-alt="346 Minutes Later"}

### on bridges

While there isn't an out-and-out statement like,

> "you can't use R inside of an ArcGIS Notebook in ArcGIS Pro"\
> -kindly do the needful, Esri Support

everything is described like:

- do your analysis in RStudio, then bring your results into ArcGIS Pro
- access and publish data on ArcGIS Online, Enterprise, or Platform
- `arcpy` can be accessed from `R` using the `reticulate` package
- enables the use of geoprocessing script tools within ArcGIS Pro

I mean, it is called the `R-ArcGIS Bridge`.\

A bridge, *bridges*, something.\
A gap? Gulf? Chasm?

It implies discrete destinations separated by something, otherwise, *impassable*. Depending on where you have lived, where you were raised, your mental image of a bridge might be big.

I'm from Texas. We have some ~~big-er~~ (not everything is bigger in Texas, that's just Texan propaganda) bridges. I was raised near an artifical reservoir flooded during the 1950s. I have many memories of the, what seemed to a young kitten, very long drive across the bridge. Looking at the level of the lake to determine how bad the drought is. Or how relieved we are that the lake is full. On rare occasions, fear that the lake might be a bridge too full.

But today, when I close my eyes, it's a looney tunes style bridge. American Southwest. Narrow wooden planks, rope bindings. I watched a lot of cartoons.\

But if I push past that visualization, I see a foot bridge.\
Spanning a stream... ...you could... ...hop over.\
What's even the point?\
So your feet don't get wet, I guess.\
Me?\
I have lots of memories of jumping over little streams, sometimes unsuccessfully (muddy antics ensue). and let's be honest. If this were something that wasn't considered *impassable*, there'd be some kind of support article about it. Surely a small blurb like,

> you can use it in an ArcGIS Pro Notebook!\
> -xoxo, Esri Support

### on beliefs

I wasn't able to find it. But in my soul, I believed it was possible. So I began to work.

![](/img/posts/2026-10-07-6-months-later.webp){fig-alt="6 Months Later"}

*The year is 2027. San Diego.*\
*We're on the main stage.*\
*I'm wearing a blue sweater. Khaki pants.*\

*Jack glares at me and then starts in on his clever intro like,*\
*"I am just so humbled by how all of you use this technology to truly transform this planet. Go ahead and give yourself a round of applause. Introduce yourself to your neighbor. Tell them your mother's maiden name. The street where you grew up on. Okay. That's enough. Ha ha this is my polite laugh. Seriously. Ahem.*\
*R you ready kids!?"*\

*The crowd chants enthusiastically back, "AYE AYE CAPTAIN!"*\

*Jack crosses the main stage impossibly fast.*\
*He scoops me up into his arms*\
*For one unexpected, blissful moment, I'm^&ensp;weightless?&ensp;it's&ensp;^*|*~&ensp;a&ensp;suplex.~*\

*Ribs shatter. Vertebrae rupture.*\
*Something in my mouth, metallic, warm.*\
*Jack bellows into the crowd,*\
*"I can't hearrrr you!"*\

*My vision begins to tunnel and fade.*\
*The crowd roars, "AYE AYE CAPTAIN!"*\

## if nautical nonsense be something you wish

So. Yeah. How do we get there?\
Well. We'll have to participate in a little bit of nonsense.\

And by nonsense, I mean, the wonderful magic of `conda`!

![](/img/posts/2026-10-07-magic.gif){fig-alt="Shia LeBouf Magic Meme, CONDA superimposed over the word MAGIC"}

So if you're reading this. You probably already have `R` installed on your workstation. Probably. Or. You could be a bit more like me. A Pythonista in your day job that has... ...other interests.

![](/img/posts/2026-10-07-other-interests.jpg){fig-alt="distracted boyfriend meme, python logo superimposed on girlfriend, feralcatcolonistcatcolonist superimposed on boyfriend,`R` logo superimposed on other woman"}

And by other interests, I mean, the tidy tidiness of the Tidiverse, the magrittr pipe, and chained operations.

And in this situation, maybe you don't have `R` on your workstation because you haven't yet had a workflow that you can shoehorn into an excuse to using `R`. Well now you do!

If I wasn't concerned about making an obnoxiously long post, then I'd just point you to any of the Esri documentation that already exists:

- <https://developers.arcgis.com/r-bridge/installation>
- <https://www.esri.com/en-us/training/catalog/67fe7b30a930b8d1449f4e28/introduction-to-the-rarcgis-bridge>

Since this is an [exactly how to do the thing article]{.smallcaps}, it behooves me to walk through, uh, exactly how to do the thing.\
We'll assume you're using ArcGIS Pro on a Windows machine.

### installing `R`
You *should* try and source `R` from *CRAN*, The Comprehensive R Archive Network, <https://cran.r-project.org/>, in the parlance of Python, it's kind of like `pip`. There are other ways to source it but we'll stick with this, the most common path.

- from the home page, navigate to the `Download R for Windows` link
- navigate to the `install R for the first time` link
- the first, top link says `Download R-4.6.1 for Windows` (as of 10/08/2026)
    - the release cadence is normally one minor release per year
- this will download a `.exe` named after the version like: `R-4.6.1-win.exe`

:::{.callout-note}
Administrative Privileges: 
activating the `.exe` without administrative rights will produce the following pop-up:

![](/img/posts/2026-10-07-r-admin-popup.png){fig-alt="Information You should be logged in as an administrator when install `R` Note: A full `R` installation requires administrative privileges, and it appears that those are not available. If you continue with this installation, you will not be able to associate `R` with `.RData` files. Installation mut be made to a directory where you have write permission."}

it won't be a deal breaker for what we're doing, but if you need that little oomph then discuss with your system administrator.
:::

**tl;dr - spam `Next` until done**

- click Next
    - read the GNU GENERAL PUBLIC LICENSE
- the default location will be some place that you have write access to, the directory will be named like:
    - `R\R-4.6.1`
- this window is for either a `user` or `custom` installation
    - for our purposes a `user` installation is fine
    - click Next
- this window is for customizing startup options
    - select "No (accept the defaults)"
    - click Next
- this window is for selecting a Start Menu Folder
    - again, the default "R" is fine
    - click Next
- this window is for "additional tasks" 
    - all of these are fine
    - click Next

Whew. Hopefully that took longer for me to type than it took for you to click through. I mean. You read the entire license right? Right!? Anyway. The installer will, uh, install R. It's fairly fast. It'll have you click Finish to exit the setup wizard. Do we still call them wizards?

![](/img/posts/2026-10-07-a-few-minutes-later.webp){fig-alt="A Few Minutes Later"}

`R` is installed! Yay!

The next bit is something of a choose-your-own-adventure. Let's not make a big deal out of it.

### installing the `R-ArcGIS Bridge` from ArcGIS Pro

- open ArcGIS Pro
- click the `Settings` tab in the left ribbon
- in the new context, click the `Options` tab in the left ribbon
    - this opens the `options` window
- scroll down the left window and click `Geoprocessing`
    - this opens geoprocessing options in the right window
    - scrolling down the right window, at the very bottom you'll see: `R-ArcGIS Support`
- this section will begin to scan your computer and *should* identify all of your`R`home directories
    - if you've been following along, there should be only one
    - if you have several, then, you have several, from the drop-down select the one you want to connect
- after the `R` Home directory has been detected a message beneath will prompt you to install the `ArcGIS R integration package`
    - click the box icon
    - select `Install package from the Internet`
    - a pop-up
        - New 'arcgisbinding' version 1.0.1.311 is available.
        - support for ArcGIS Pro 3.5+ would you like to install it
    - click Yes
    - a geoprocessing-style output appears and will prompt to close when the download is complete
- the message beneath the `R` Home directory will now read that the arcgisbinding package is installed
    - these libraries have been installed in your `R` Home directory

![](/img/posts/2026-10-07-5-minutes-later.webp){fig-alt="5 Minutes Later"}

`R-ArcGIS Bridge` is installed! Yay!

### installing the `R-ArcGIS Bridge` from *not* ArcGIS Pro

Using `RStudio`, your IDE of choice, or `R.exe` from the install directory, get into your `R` console and run the following:

```r
install.packages("arcgis", repos = c("https://r-arcgis.r-universe.dev", "https://cloud.r-project.org"))
install.packages("arcgisbinding", repos = "https://r.esri.com", type = "win.binary")
```

cue matrix-style terminal outputs. You can review your ArcGIS Pro using the steps above to confirm that the `R-ArcGIS Bridge` is fully installed.

![](/img/posts/2026-10-07-12-seconds-later.webp){fig-alt="12 Seconds Later"}

`R-ArcGIS Bridge` is installed! Yay!

### the inner machinations of [ArcGIS Pro] are an enigma

This might be an excellent part to jump-cut back to, why I think it's possible to use `R` in an ArcGIS Pro Notebook.

An ArcGIS Notebook is a Jupyter Notebook. And while most people just think, Jupyter Notebook == much cooler than running code in a terminal. What you might not know, is that Project Jupyter is an open-source project designed to support `JU`lia `PY`thon and `R`. Naturally, one might expect that Julia and R could just be spun up in any old Notebook. And naturally, you'd be wrong.\

At least in Esri-landia. No Julia kernel. No R kernel.\
Fine fine.\
But.\
What about some... ...Notebook Magic?

![](/img/posts/2026-10-07-notebook-magic.gif){fig-alt="Shia LeBouf Magic Meme, NOTEBOOK appears above the word MAGIC"}

And in what could easily be, and, ugh, likely will, be another post, we need to understand a small bit about notebook magic commands.\
And by a small bit, I'll say, using a single modulo `%` or a double modulo `%%` within a notebook allows you access to a variety of magics-- --utilities that can do a variety of things:\

- `%pip` installs,\
- `%load` a file,\
- `%run` a notebook,\
- measure a cell's execution time with `%%timeit`

All of these, are implemented via the Python kernel.\
And are totally usable inside of the much vaunted ArcGIS Pro Notebook.\
Within the standard magics, you can even... ...run a different language.\
bash, sh, javascript, ruby, perl, latex, markdown, html 

Outside of the sanctioned magic. There exists... ...more arcane spells.\
Of these, a certain Python library `rpy2` implements\
`Rmagic` `%%R`

![](/img/posts/2026-10-07-not-from-arcgis-pro.jpg){fig-alt="Anakin Palpatine meme; Anakin: is it possible to conda install rpy2? Palpatine: not from arcgis pro"}

Akshually.\
You can use the arcgis pro package manager to add `rpy2` into a cloned `arcgispro-py3` kernel\

- open the package manager
- clone `arcgispro-py3`, let's call it `arcgispro-py-3-rpy2`

![](/img/posts/2026-10-07-15-minutes-later.webp){fig-alt="15 Minutes Later"}

- go to add packages
- select `rpy2`
- click install
- click update
- update failed

![](/img/posts/2026-10-07-arcgispro-py-3-rpy2.jpg){fig-alt="Gru's plan meme; clone arcgispro-py3, package install rpy2 package update rpy2, Validating 'rpy2' package for update - Fail, Validating 'rpy2' package for update - Fail"}

Whatever.\
We didn't want it updated anyway.\
Let's just follow the `rp2` documentation and unpack that sweet sweet `R` magic.\
We'll open an ArcGIS Notebook.

> Step 1
```python
%load_ext rpy2.ipython
```

![](/img/posts/2026-10-07-and-its-gone.gif){fig-alt="South Park margaritaville and its gone meme, it reads aaaaannnnd ArcGIS Pro Quit"}

Alright alright.\
I'mma let you have that one.\
But.\
Rolls up sleeves and unfurls a small wooden wand.\
How about a taste of `%pip` magic!?

> ~~Step 1~~ Step 0
```python
%pip install rpy2
# Note: you may need to restart the kernel to use updated packages.
```
> Step 1
```python
%load_ext rpy2.ipython
```

![](/img/posts/2026-10-07-and-its-gone.gif){fig-alt="South Park Margaritaville and its gone meme, it reads aaaaannnnd ArcGIS Pro Quit"}

And here, we finally get the pay-off for the section title.

:::{.callout-note}
As a closed-source product, we don't **akshually** know what's going on.

We can guess about some things, we can test about some things, and we can get some bits and pieces of understanding based on what features are and are not available. In ArcGIS Pro, we know that the Python.exe is tightly integrated within the product. It's the reason that ArcGIS Notebooks are slow to load. It's the reason why separate ArcGIS Notebooks share all the same variable data within the same ArcGIS Pro session (it's kind of hilarious). It's the reason you can't switch conda environments without re-opening ArcGIS Pro.

And if that conda environment stops working correctly, well, the everything else just stops working too.

Some of this is definitely an Esri problem. And some of this is just part of the weakness of conda (which is why it's not the only game in town anymore). We don't often talk about how we have to be cognizant of all the Esri-specific dependencies that ArcGIS Pro has going on. And it's not the most common thing to be a package manager expert (*don't look at me, I am most certainly not*).

So within ArcGIS Pro, the package manager is enforcing the Esri channel to prevent the user from breaking the distribution. In this very specific instance, we end up in a situation where the `conda` version of `rpy2` is incompatible with the version of `R` we downloaded. Although it's really funny to just imagine throwing out a `pip` command like a gladiator throwing sand in their opponent's eyes; and while, mixing your `pip` and `conda` is not best practice, some times, it's the best way.
:::

So once we know some of that, we have a better understanding as to why some things that we're doing just won't work.\

## then drop on the deck and flop like a fish

Which isn't to say, what we're trying to do won't work.

![](/img/posts/2026-10-07-a-few-moments-later.webp){fig-alt="A Few Moments Later"}

If you were to open that ArcGIS Notebook as a Jupyter Notebook in, let's say, VSCode, pointed to our cloned kernel `arcgispro-py-3-rpy2`. Running that same cell from above:

```python
%pip install rpy2
```

You'd get an output like:

```
Requirement already satisfied: rpy2 in c:\users\feralcatcolonist\appdata\roaming\python\python311\site-packages (3.6.8)Note: you may need to restart the kernel to use updated packages.

Requirement already satisfied: rpy2-rinterface>=3.6.7 in c:\users\feralcatcolonist\appdata\roaming\python\python311\site-packages (from rpy2) (3.6.7)
Requirement already satisfied: rpy2-robjects>=3.6.5 in c:\users\feralcatcolonist\appdata\roaming\python\python311\site-packages (from rpy2) (3.6.5)
Requirement already satisfied: packaging in c:\users\feralcatcolonist\appdata\local\esri\conda\envs\arcgispro-py3-rpy2\lib\site-packages (from rpy2) (24.2)
Requirement already satisfied: cffi>=1.15.1 in c:\users\feralcatcolonist\appdata\local\esri\conda\envs\arcgispro-py3-rpy2\lib\site-packages (from rpy2-rinterface>=3.6.7->rpy2) (1.17.1)
Requirement already satisfied: jinja2 in c:\users\feralcatcolonist\appdata\local\esri\conda\envs\arcgispro-py3-rpy2\lib\site-packages (from rpy2-robjects>=3.6.5->rpy2) (3.1.5)
Requirement already satisfied: tzlocal in c:\users\feralcatcolonist\appdata\roaming\python\python311\site-packages (from rpy2-robjects>=3.6.5->rpy2) (5.4.4)
Requirement already satisfied: pycparser in c:\users\feralcatcolonist\appdata\local\esri\conda\envs\arcgispro-py3-rpy2\lib\site-packages (from cffi>=1.15.1->rpy2-rinterface>=3.6.7->rpy2) (2.21)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\feralcatcolonist\appdata\local\esri\conda\envs\arcgispro-py3-rpy2\lib\site-packages (from jinja2->rpy2-robjects>=3.6.5->rpy2) (3.0.2)
Requirement already satisfied: tzdata in c:\users\feralcatcolonist\appdata\roaming\python\python311\site-packages (from tzlocal->rpy2-robjects>=3.6.5->rpy2) (2026.4)
```

A very careful reading of the above will show that, these paths, are not the conda paths. Navigating to that directory, and comparing it to the cloned directory:

`C:\Users\feralcatcolonist\AppData\Roaming\Python\Python311\site-packages`
`C:\Users\feralcatcolonist\AppData\Local\ESRI\conda\envs\arcgispro-py3-rpy2\Lib\site-packages`

We see a few differences.\
And maybe, we want to ask why?
But we won't.

### you don't need a license to [copy-paste] a sandwich

And in what could only be described as an impossibly cerebral, high stakes game of 4-D chess,\
I copied and pasted all of the directories and files that shared the same timestamp as `rpy2` from the `pip` `site-packages` into the `site-packages` directory of my cloned environment `arcgispro-py3-rpy2`.

these little fellas:

> ```
> rpy2/
> rpy2_rinterface-3.6.7.dist-info/
> rpy2_robjects-3.6.5.dist-info/
> rpy2-3.6.8.dist-info/
> tzdata/
> tzdata-2026.4.dist-info/
> tzlocal/
> tzlocal-5.4.4.dist-info/
> _rinterface_cffi_abi.py
> _rinterface_cffi_api.pyd
> ```

from here:\
`C:\Users\feralcatcolonist\AppData\Roaming\Python\Python311\site-packages`\
into here:\
`C:\Users\feralcatcolonist\AppData\Local\ESRI\conda\envs\arcgispro-py3-rpy2\Lib\site-packages`

and with that little bit of dark wizardry out of the way, we can re-open ArcGIS Pro and pop back into that ArcGIS Notebook. 

![](/img/posts/2026-10-07-r-in-arcgis-notebook.gif){fig-alt="using R in an ArcGIS Notebook"}

and here's some of what's above in a more legible format. Going cell by cell it looks like this.

```python
# first you'll need to load the rpy2 notebook extension
%load_ext rpy2.ipython
```

```python
%%R # this tells the interpreter to treat the entire cell as an R cell
cat("Hello, World!\n") # yay!
print(R.version.string) # R works!
install.packages("ggplot2", repos = "https://cloud.r-project.org") # you can install packages
library(ggplot2) # load libraries
ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point() #rpy2 comes with ggplot2 magic
```

```python
%%R # and here's the R ArcGIS Bridge
gimme_esri <- c("arcgisbinding", "arcgis") # inside of
lapply(gimme_esri, library,character.only = TRUE) # you know
print(arc.check_product()) # ArcGIS Pro
arcgis_packages(include_self = TRUE) # perhaps, the R ArcGIS [Foot] Bridge
```

And there you have it.

![](/img/posts/2026-10-07-r-in-arcgis-notebook-rainbow.gif){fig-alt="Spongebob imagination meme, the phrase, R in an ArcGIs Notebook is superimposed over the rainbow"}

So what's the logical next step? Probably an entire series of using the R ArcGIS Bridge.

![](/img/posts/2026-10-07-several-song-filled-hours-later.webp){fig-alt="Several Song Filled Hours Later"}

But first. I have some pixies to catch.

## Further Reading
- Aydin, O., Pavlushko, D., Walbridge, S., Kopp, S., & Janikas, M. V. 2024. "arcgisbinding: An R package for integrating R and ArcGIS." Environmental Modelling & Software 172: 105904. <https://doi.org/10.1016/j.envsoft.2023.105904>
- R-ArcGIS Bridge, Esri documentation <https://developers.arcgis.com/r-bridge/>
- Introduction to the R-ArcGIS Bridge, Esri Academy<https://www.esri.com/en-us/training/catalog/67fe7b30a930b8d1449f4e28/introduction-to-the-rarcgis-bridge>
- documentation for rpy2 <https://rpy2.github.io/doc/latest/html/index.html#>