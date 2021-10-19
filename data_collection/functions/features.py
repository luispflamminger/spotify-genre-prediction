import requests
import math
import os
import json
import copy

def getFeaturesOfTracks(requests_session, auth_token, data_object, write_to_file=False, path_to_file=''):

    #Establishing the requests session
    http = requests_session

    #Establishing given object
    data = data_object

    for category in data["categories"]:
        
        for playlist in category["playlists"]:
            
            track_ids = [[]]

            for track in playlist["tracks"]:
                
                track_ids[len(track_ids)-1].append(track["id"])
            
                if len(track_ids[len(track_ids)-1]) > 99:
                    track_ids.append([])

            all_track_features = []

            for page in track_ids :
                comma_seperated_ids = ",".join(page)

                url = f"https://api.spotify.com/v1/audio-features?ids={comma_seperated_ids}"
                headers = { 'Authorization': f'Bearer {auth_token}' }

                try:
                    response = http.request("GET", url, headers=headers, data={})
                    if response.status_code != requests.codes.ok:
                        raise Exception
                except Exception as e:
                    raise SystemExit(e)
                
                #Combine lists
                all_track_features = all_track_features + response.json()["audio_features"]
            i = 0
            for track in playlist["tracks"]:

                for entry in all_track_features:
                    if entry is not None and track["id"] == entry["id"] and entry["type"] == "audio_features":
                        track["features"] = copy.copy(entry)
                        del track["features"]["id"]
                        del track["features"]["type"]
                        del track["features"]["uri"]
                        del track["features"]["track_href"]
                        del track["features"]["analysis_url"]
                        break
                i += 1

        if write_to_file == True:
            with open(path_to_file, 'w') as outfile:
                json.dump(data, outfile, indent=2)

    return data