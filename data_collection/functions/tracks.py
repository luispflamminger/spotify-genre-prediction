import requests
import math
import os
import json

def getTracksOfPlaylists(requests_session, auth_token, data_object, write_to_file=False, path_to_file=''):

    #Establishing the requests session
    http = requests_session

    #Establishing given object
    data = data_object

    for category in data["categories"]:
        
        for playlist in category["playlists"]:

            playlist_id = playlist["id"]
            url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?market=US&limit=2&offset=0&fields=items(track(name,id,album(name,id),artists)),total&additional_types=track"
            headers = { 'Authorization': f'Bearer {auth_token}' }

            try:
                response = http.request("GET", url, headers=headers, data={})
                if response.status_code != requests.codes.ok:
                    raise Exception
            except Exception as e:
                raise SystemExit(e)
            
            trackAmount = response.json()["total"]

            #Calculate number of pages with 50 items
            pages = int(math.ceil(trackAmount/50))

            #Initialize playlist attribute
            playlist["tracks"] = []

            for page in range(pages):
                url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?market=US&limit=50&offset={page * 50}&fields=items(track(name, id, album(name, id), artists)), total&additional_types=track"
                headers = { 'Authorization': f'Bearer {auth_token}' }

                try:
                    response = http.request("GET", url, headers=headers, data={})
                    if response.status_code != requests.codes.ok:
                        raise Exception
                except Exception as e:
                    raise SystemExit(e)

                i = 0
                for item in response.json()['items']:
                    track = item["track"]
                    
                    #Some track elements will have value null, this throws exception
                    if track is None:
                        continue

                    artists = []

                    for artist in track["artists"]:
                        artists.append({
                            "id" : artist["id"],
                            "name" : artist["name"]
                        })

                    playlist["tracks"].append({
                        "id": track["id"],
                        "name": track["name"],
                        "album" : {
                            "id" : track["album"]["id"],
                            "name" : track["album"]["name"]
                            },
                        "artists" : artists
                     })
                    i += 1

        if write_to_file == True:
            with open(path_to_file, 'w') as outfile:
                json.dump(data, outfile, indent=2)

    return data