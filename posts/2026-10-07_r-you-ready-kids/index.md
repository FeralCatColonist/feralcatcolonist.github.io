---
title: "[R] You Ready, Kids?"
description: "Who lives in a [kernel] under the [ArcGIS Pro Notebook]?"
date: "2026-10-07"
image: "/img/posts/2024-12-27-arcade-machine.png"
categories: ["ArcGIS", "R", "Conda"]
aliases: ["/2026/10/07/r-you-ready-kids.html"]
---
I try not to be a competitive person. Most of the time I'm fairly successful, I can focus on me and let other things lie. Unfortunately, there are a few situations that tend to goad me into action; creating, what some might term a, *hold my beer* moment. Mostly these are some flavor of:
> item/action/technique doesn't work in `<insert thing here>`
A few weeks ago, I was whisked down into the depths of single-minded competition (with no one actually except the shade of some gatekeeper). In the GIS Discord, it started with a stray comment:
> "I found a non-esri result, but it bluntly told me that you can't do R in arcgis notebooks"
My immediate response was:
> Who wants to use a filthy ArcGIS notebook anyway? Literally the worst way to jupyter
^^^ and as petty as my comment was, I was already hooked.

## absorbent and yellow and porous is he
It turned over and over in my mind's eye.
*I doubt it's impossible.* But I had just read a bunch of documentation.
*Squints.* I have a Mendela Effect memory of an ArcGIS Notebook having a kernel switch button for R. 

While there isn't an out-and-out statement that, "you can't use R inside of an ArcGIS Notebook in ArcGIS Pro", everything is described like:
- do your analysis in RStudio, then bring your results into ArcGIS Pro
- `arcpy` can be accessed from R using the  `reticulate`
- R-based GP script tools are defined in a standalone R script file
I mean, it is called the R-ArcGIS Bridge. A bridge, *bridges*, something. A gap? Gulf? Chasm? It implies discrete destinations. Depending on where you have lived, where you were raised, your mental image of a bridge might be big. I'm from Texas. We have some big-er (not everything bigger in Texas, that just Texan propaganda) bridges. I was raised near an artifical reservoir flooded during the 1930s. I have many memories of the very long drive across the bridge. Looking at the level of the lake to determine how bad the drought is. Or how relieved we are that the lake is full.

But when I close my eyes. It's a looney tunes style bridge. I watched a lot of cartoons. When I push past that visualization, I see a foot bridge. Spanning a stream you could hop over. What's the point? So your feet don't get wet, I guess. Me? I have lots of memories of jumping over little streams (sometimes unsuccessfully, muddy antisc ensue).

## let's get our feet wet
and let's be honest. If this were something that wasn't considered impossible, there'd be some kind of support article about it. Surely a small blurb like, you can use it in an ArcGIS Pro Notebook! We're on the main stage, Jack has some clever intro like, R you ready kids!? The crowd chants enthusiastically back, "AYE AYE CAPTAIN!"


## Incrementing Number of Features
At previous organizations, I've done some fancy things with AssetIDs. And by fancy, I mean dumb. And by dumb, I mean, over-engineered based on spatial positioning for a grid system that was subject to change. I really like the pattern our staff came up with, it bakes in a create date, who collected it, and then doesn't artificially constrain the total number of assets-- --just assumes a person doesn't collect more than 999 assets in a day. How does one increment features though? Through featuresets of course! But before we get to featuresets, it's helpful to thing about how we'd do this on the desktop.

### Filter
We would Filter our feature class using a definition query. Arcade utilizes the SQL-92 standard, which is the same used by shapefiles and file geodatabases. Some light reading can be found here:

SQL reference for query expressions used in ArcGIS—ArcGIS Pro | Documentation
[https://doc.esri.com/en/arcgis-pro/latest/help/mapping/navigation/sql-reference-for-elements-used-in-query-expressions.html](https://doc.esri.com/en/arcgis-pro/latest/help/mapping/navigation/sql-reference-for-elements-used-in-query-expressions.html)

### References
[https://www.sciencedirect.com/science/article/pii/S1364815223002906](https://www.sciencedirect.com/science/article/pii/S1364815223002906)