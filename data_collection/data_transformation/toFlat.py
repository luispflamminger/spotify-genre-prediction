import json
import pandas as pd
import os
import copy

# load json
file = open(os.path.join("data_collection", "json", "features_filtered.json"))
data = json.load(file)

# variables 
temp = {}
path = ""
result = []

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
                            
                            # loop over tracks
                            for track in playlist["tracks"]:

                                for item in track:
                                    
                                    if item != "album" and item != "artists" and item != "features":
                                        key     = f"{path}.{item}"
                                        value   = f"{track[item]}"
                                        temp[key] = value
                                    
                                    else:
                                        
                                        # album data
                                        if item == "album":
                                            
                                            for album in track["album"]:
                                                key     = f"{path}.album.{album}"
                                                value   = f"{track['album'][album]}"
                                                temp[key] = value

                                        # artist data (just name)
                                        if item == "artists":
                                            
                                            value = ""

                                            for artist in track["artists"]:

                                                if not value:
                                                    value = artist["name"]
                                                else:
                                                    value = f"{value}, {artist['name']}"
                                                

                                            key     = f"{path}.artist"
                                            temp[key] = value

                                        # track features
                                        if item == "features":

                                            for feature in track["features"]:
                                                key     = f"{path}.feature.{feature}"
                                                value   = f"{track['features'][feature]}"
                                                temp[key] = value

                                # write temp to flat json
                                # temp represents one line 
                                #print("end of track")
                                result.append(copy.copy(temp))


with open(os.path.join("data_collection", "data_transformation", "result.json"), 'w') as outfile:
    json.dump(result, outfile, indent=2)

