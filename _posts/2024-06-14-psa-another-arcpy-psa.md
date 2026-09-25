---
layout: post
title: "Another ArcPy PSA (ArcGIS Pro 3.3)"
subtitle: "I really wish I could have matched the font better"
date: 2024-06-14
background: '/img/posts/2024-06-14-update-or-die.png'
---
Just a small #ArcPy public service announcement for anyone creating a standalone environment via #conda using #ArcGISPro 3.3. The currently hosted arcpy package (`py311_arcgispro_52583`) may not work on your machine utilizing the normal conda command like:

```cmd
conda install esri::arcpy
```

You'll be alerted if this is an issue because the packages will refuse to install, instead there will be a series of cascading errors each ending with something like:

```
Runtime Error: OpenlSSL 3.0's legacy provider failed to load. This is a fatal error by default, but cryptography supports running without legacy algorithms by .
```

Luckily this isn't a deal breaker, you'll just need to specify the install order with the following commands, this assumes you are starting in (`base`) conda:

```cmd
conda create -n the-name-of-your-new-env
conda activate the-name-of-your-new-env
conda install esri::python
conda install esri::cryptography
conda install esri:arcpy
```

There ya go. Hopefully you find this and it is relatively painless. Or it gets patched and somehow you stumbled upon this and it seems a bit esoteric.

[![an image of the join or die segmented snake, the words have been altered to say "update or die"](/img/posts/2024-06-14-update-or-die.png)](/img/posts/2024-06-14-update-or-die.png)