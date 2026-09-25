---
layout: post
title: "PSA: Your ArcPy Might be Broken"
subtitle: "I went with the clickbait title this time"
date: 2023-11-08
background: '/img/posts/2023-11-08-logo-anaconda-esri.png'
---
## The less sensational title might be:
### *ArcPy Minor Upgrades are a Minor Headache.*

Two years ago I wrote [a long article](/2021-03-19-standalone-arcgis-conda.html) on how to create a standalone ArcPy environment; normally, I'd say it is worth a read but its probably out of date. I've seen a few more articles since then covering the same subject matter so I'm hoping that this a more common practice. Why am I writing this? Yesterday, Esri released a new minor update to ArcGIS Pro from `3.1.x` to `3.2.0` and judging from the **What's New** page this is one of the more feature-rich releases to the software since `2.7.x`.

[![a screenshot of the top of the documentation linked below](/img/posts/2023-11-08-doc-snippet-esri-01.png)](/img/posts/2023-11-08-doc-snippet-esri-01.png)
https://pro.arcgis.com/en/pro-app/latest/get-started/whats-new-in-arcgis-pro.htm

With a new minor release comes new binaries, meaning that any Conda environments created within the ArcGIS Pro GUI or ArcPy installations created in a standalone fashion need to be freshly installed. You'll know if this happens when you see an error like this:

[![A Conda error showing that an ArcPy version tied to ArcGIS Pro 3.1.x will not work with an ArcGIS Pro 3.2.x installation.](/img/posts/2023-11-08-cmd-snippet-01.png)](/img/posts/2023-11-08-cmd-snippet-01.png)
*A Conda error showing that an ArcPy version tied to ArcGIS Pro 3.1.x will not work with an ArcGIS Pro 3.2.x installation.*

Normally one could just run a command like:

```cmd
conda update some-library
```

Because of the binary situation above, this does not work with the ArcPy library. We have two options for removing and re-installing ArcPy which I'll cover. Esri has a convenience feature for "upgrading" your ArcPy environment; however, the actual mechanism works like this:


[![a screenshot of the esri documentation outlining the upgrade process](/img/posts/2023-11-08-doc-snippet-esri-02.png)](/img/posts/2023-11-08-doc-snippet-esri-02.png)
*This update process deletes the environment... ...and re-creates it *

If you are using ArcPy in a standalone kernel for Python, and you have, or are planning to, install the new minor release update (3.2) to ArcGIS Pro you will need to reinstall ArcPy in your Conda environment. Let's look at a few options that you have for performing the reinstall; we'll imagine a few different scenarios.

## Scenario 0 - You Can do a Standalone Installation of ArcPy!?
Yes. It's super easy and this is how I do it! From an Anaconda prompt window, we'll do the following using the placeholder ENV_NAME for the name of your standalone Conda environment. Feel free to name it whatever you like.

```cmd
conda create -n ENV_NAME
conda activate ENV_NAME
conda install -c esri arcpy
```

The first line creates the environment, you'll need to press the "y" key and then the "enter" key to complete the installation. The second line will activate this new environment. The third line installs ArcPy and all of its related packages into it, this also includes the ArcGIS API for Python.

[https://anaconda.org/esri/arcpy](https://anaconda.org/esri/arcpy)

## Scenario 1 - A Simple Scenario
I just installed ArcPy and nothing else. Congratulations! You can remove and re-install ArcPy without thinking about it too hard.

```cmd
conda deactivate ENV_NAME
conda remove -n ENV_NAME --all
conda install -c esri arcpy
```

The first line deactivates your environment if it is open already. The second line removes all packages. The last line will reinstall ArcPy. That's it, your environment will continue to work as expected and won't break any of your scheduled tasks if you had them written against the python.exe path within your kernel.

## Scenario 2 - I, uh, Installed a Few Other Packages
This doesn't surprise me. Anaconda is a package manager. You use it to manage packages. You like to dabble in GeoPandas and other libraries of substance. Me too. If you know exactly what you're looking for, you can trawl through a .yaml file:

```cmd
conda activate ENV_NAME
cd "some path where you want the exported file"
conda env export > some_file_name.yml
```

The ArcPy library has a lot of dependencies so browsing it like this isn't really my cup of tea. Although, a .yaml is a great way to share your environment with someone else. I think an easier way to look at your package installations is to look at your revision history. This is Anaconda's version control, when you access it, the output is a numbered list of the libraries and their versions installed at each command:

```cmd
conda activate ENV_NAME
conda list --revisions
```

This batched version of downloads should help you to figure out which libraries you downloaded (and in what order) so you have a better idea of how you need to re-create your environment. ArcPy is normally the first install I make after creating the environment, so I rolled back my environment and then re-installed ArcPy like this:

```cmd
conda install --revision 0
conda install -c esri arcpy
```

Your syntax will likely be different depending on the number if libraries you need to include and in what order of installation those happened.

And it's kind of that easy. Admittedly, not as easy as upgrading a library with the update command but such is the life of a licensed software library.

[![a screenshot of the top of the documentation linked below](/img/posts/2023-11-08-logo-anaconda-esri.png)](/img/posts//img/posts/2023-11-08-logo-anaconda-esri.png)