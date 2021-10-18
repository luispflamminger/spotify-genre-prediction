import json
import pandas as pd
import os

# load json
file = open(os.path.join("tests_martin", "test1", "jsonFormatExample.json"))
data = json.load(file)

# variables 
temp = {}
path = ""

# loop over categories
for category in data["categories"]:

    path = "category"

    for item in category:

            if item != "playlists":
                key     = f"{path}.{item}"
                value   = f"{category[item]}"
                temp[key] = value 

            else:
                
                path = f"{path}.playlist"
                
                #loop over playlist
                for playlist in category["playlists"]:

                    for item in playlist:

                        if item != "tracks":
                            key     = f"{path}.{item}"
                            value   = f"{playlist[item]}"
                            temp[key] = value

                        else:

                            path = f"{path}.track"

                            for track in playlist["tracks"]:

                                for item in track:
                                    
                                    if item != "album" & item != "artists":
                                        key     = f"{path}.{item}"
                                        value   = f"{playlist[item]}"
                                        temp[key] = value










print(temp)



