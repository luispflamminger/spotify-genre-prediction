import requests
import math
import os
import json

def getPlaylistsForCategories(requests_session, auth_token, data_object, write_to_file=False, path_to_file=''):

    #Establishing the requests session
    http = requests_session

    #Establishing given object
    data = data_object

    for category in data["categories"]:
        
        category_id = category["id"]
        url = f"https://api.spotify.com/v1/browse/categories/{category_id}/playlists?country=US&limit=1&offset=0"
        headers = { 'Authorization': f'Bearer {auth_token}' }

        try:
            response = http.request("GET", url, headers=headers, data={})
            if response.status_code != requests.codes.ok:
                raise Exception
        except Exception as e:
            raise SystemExit(e)
        
        categoryAmount = response.json()["playlists"]["total"]

        #Calculate number of pages with 50 items
        pages = int(math.ceil(categoryAmount/50))

        #Initialize playlist attribute
        category["playlists"] = []

        for page in range(pages):
            url = f"https://api.spotify.com/v1/browse/categories/{category_id}/playlists?country=US&limit=50&offset={page * 50}"
            headers = { 'Authorization': f'Bearer {auth_token}' }
            try:
                response = http.request("GET", url, headers=headers, data={})
                if response.status_code != requests.codes.ok:
                    raise Exception
            except Exception as e:
                raise SystemExit(e)

            i = 0
            for playlist in response.json()["playlists"]["items"]:
                if playlist["type"] == "playlist":
                    category["playlists"].append({
                        "id": playlist["id"],
                        "name": playlist["name"]
                    })
                i += 1

        if write_to_file == True:
            with open(path_to_file, 'w') as outfile:
                json.dump(data, outfile, indent=2)

    return data