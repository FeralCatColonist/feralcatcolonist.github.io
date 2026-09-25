---
layout: post
title: "Maybe the Real Treasure was the Deprecations We Made Along the Way?"
subtitle: "change my mind."
date: 2024-11-17
background: '/img/posts/2024-11-07-meme-all-map-viewer-items.png'
---
My toxic trait is that I am overly fond of novelty. In the technology field, this is something of a boon except for all the technical debt we leave in our wake. In the hashtag#Esri-verse, everyone loves talking about the impending sunset of ArcMap. Today, I wanted to take a moment to share another deprecation that affects the ArcGIS ecosystem. Namely, Map Viewer Classic. Some might say, best map viewer. RIP Map Viewer Classic.

https://support.esri.com/en-us/knowledge-base/deprecation-map-viewer-classic-deprecation-000030662

Anyway, in Q1 of 2026, these *classic* Web Map items will no longer be available in ArcGIS Online. So, the question for GIS professionals that administer an ArcGIS Online or ArcGIS Enterprise deployment, is, how do you find out which Web Map Viewers are *classic* vs which ones are the *new* Web Map Viewer?


Anakin Padme Meme:
panel1 Anakin: you need to convert all of your web map viewer classics to the new web map viewer
panel 2 Padme: that should be something we can filter against or see visually right?
panel 3 Anakin staring: no text
panel 4 Padme: that should be something we can filter against or see visually right?
You could just, go and look at them right? Right?


You could, go in and open every Web Map and then make sure to re-save it in the *new* Web Map Viewer. Which, spoiler alert, you'll (or preferably your users) need to do anyway. But you could be running into the overhead of accidentally saving items that are already *new* Web Map Viewer.


All Map Viewers Look the Same, Change My Mind.
*How would we even know the difference looking at it like this?*


But, what if? You had a map, of sorts, to show you which items needed to be fixed?


Dataframe showing that Web Map items are different depending on how they were created, with Web Map Viewer new or classic.
*If you know where to look, it's easy to see the difference.*


Behold. Some code that does just that. Assuming you are logged into ArcGIS Pro with the account based on the organization you're looking to audit, then running this is fairly straight forward. We can still walk through the code to de-mystify it a little.

```python
import arcgis
import pandas as pd
import time

gis = arcgis.gis.GIS("pro")
content_list = gis.content.search(query="*", item_type="Web Map", max_items=-1)
print(f"Org-wide there are {len(content_list)} Web Map items")
map_viewer_classic_items = {}
i = 0
for item in content_list:
    time.sleep(1)
    item_data = item.get_data()
    if "authoringApp" not in item_data:
        continue
    authoringApp = item_data["authoringApp"]
    if authoringApp == "WebMapViewer":
        i += 1
        map_viewer_classic_items[i] = [
            item.itemid,
            authoringApp,
            item.numViews,
            item.owner,
            item.title,
        ]
df = pd.DataFrame.from_dict(
    map_viewer_classic_items,
    orient="index",
    columns=["itemid", "authoringApp", "views", "owner", "title"],
)
df.to_csv(r"C:\some-folder-path\WebMapViewer-manifest.csv", index=False)
print(f"\trecorded a total of {i} Map Viewer Classic items")
```

Okay, so the first few lines are importing the libraries we need, fairly standard stuff. We use arcgis for ArcGIS ecosystem things, we'll use pandas to ultimately shuttle the data into a spreadsheet, and lastly, we use the time library to rate-limit our API calls against our ArcGIS deployment.

```python
import arcgis
import pandas as pd
import time
```

Then we'll log into our ArcGIS deployment (Online or Enterprise) based on whatever organization we're currently logged in to. There are other authentication methods that I won't discuss that can be found here:

https://developers.arcgis.com/python/latest/guide/working-with-different-authentication-schemes/

```python
gis = arcgis.gis.GIS("pro")
```

Next we'll search through all of our organization's ArcGIS items, with a filter based on, is it a Web Map? Unfortunately, that by itself doesn't get us where we need to go. Because I like to pretend we're in the Matrix, I tend to use print statements to let me know where we're at in the program. This f-string lets us know the number of returned items that matched our search for Web Maps in the organization.

```python
content_list = gis.content.search(query="*", item_type="Web Map", max_items=-1)
print(f"Org-wide there are {len(content_list)} Web Map items")
```

This next part looks like a lot, but it isn't so bad.

We make an empty dictionary called `map_viewer_classic_items` and an integer called `i`, we'll use these to create our data structure. For every item returned by the `content_manager` in the `content_list` variable, we'll perform the following actions:

1. time.sleep(1) | sleep for one second, this makes sure that we avoid hitting our ArcGIS Deployment too frequently and returning a 404 error
2. item_data = item.get_data() | this is the arcgis library, it is a call that gets the JSON data backing an item, it is returned as a dictionary that we'll call item_data
3. if "authoringApp" not in item_data: | check if the key authoringApp is in the dictionary item_data, this is important because not every kind of Web Map has that authoringApp key, and assuming it is there can cause a KeyError exception. If the current item doesn't have that parameter, we continue the for loop to the next iteration
4. authoringApp = item_data["authoringApp"] | this is an intermediate variable, we're grabbing the value associated with the authoringApp key for layer use in the loop
5. if authoringApp == "WebMapViewer": | we check to see if the value of the authoringApp key is WebMapViewer. The new Web Map Viewer's value is ArcGISMapViewer. So if it is a classic Map Viewer, we'll increment our i by 1. We use this value to create new entries in our dictionary
6. map_viewer_classic_items[i] = | here we write a new dictionary entry per each classic Web Map Viewer that we found, and populate it with values from the item_data dictionary along with the value of the authoringApp key-- --this is a little redundant but I originally was looking for any type of Web Map and was filtering the results in a spreadsheet later.

```python
map_viewer_classic_items = {}
i = 0
for item in content_list:
    time.sleep(1)
    item_data = item.get_data()
    if "authoringApp" not in item_data:
        continue
    authoringApp = item_data["authoringApp"]
    if authoringApp == "WebMapViewer":
        i += 1
        map_viewer_classic_items[i] = [
            item.itemid,
            authoringApp,
            item.numViews,
            item.owner,
            item.title,
        ]
```

And we're past the hard part! Kind of. This next thing does a lot. We use a standard pandas function `from_dict()` to create a dataframe from a dictionary. We'll use the `map_viewer_classic_items` dictionary that we populated in the for loop above, then we'll use the index orientation, which means that each dictionary record will correspond to a record row in the dataframe, then we'll give a list of names for the columns that correspond to the item's data attributes.

```python
df = pd.DataFrame.from_dict(
    map_viewer_classic_items,
    orient="index",
    columns=["itemid", "authoringApp", "views", "owner", "title"],
)
```

Whew. And we're really doing this because we want to push it down to a spreadsheet using an easy button, to_csv() is a panda's function that writes a dataframe to a CSV. Then we'll print another f-string function which includes a count i of the total number of items written to the .csv that we exported. And you could just open the .csv to find out but. Matrix.

```python
df.to_csv(r"C:\some-folder-path\WebMapViewer-manifest.csv", index=False)
print(f"\trecorded a total of {i} Map Viewer Classic items")
```

Anyway. That's the thing. You have a year or so to go out and fix it.


Here's a picture of my pretty code because LinkedIn likes to butcher code and won't put in language specific options.
*We're going to need a bigger [GIS Administrator]*