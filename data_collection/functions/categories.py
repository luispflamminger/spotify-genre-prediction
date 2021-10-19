import requests
import math
import os
import json

def getAllCategories(requests_session, auth_token, data_object, use_category_filter=False, category_filter=None, write_to_file=False, path_to_file=''):
    
    #Establishing the requests session
    http = requests_session

    #Establishing given object
    data = data_object
    
    #First API call used to get the total amount of categories
    headers = { 'Authorization': f'Bearer {auth_token}' }
    url = "https://api.spotify.com/v1/browse/categories?country=US&locale=en_US&limit=1"
    
    try:
        response = http.request("GET", url, headers=headers, data={})
        if response.status_code != requests.codes.ok:
            raise Exception
    except Exception as e:
        raise SystemExit(e)

    response.raise_for_status()
    categoryAmount = response.json()["categories"]["total"]

    #Calculate number of pages with 20 items
    pages = int(math.ceil(categoryAmount/50))
    data = {"categories": []}

    #Second call gets all categories
    for x in range(pages):
        url = f"https://api.spotify.com/v1/browse/categories?country=US&locale=en_US&limit=50&offset={x * 50}"
        
        try:
            response = http.request("GET", url, headers=headers, data={})
            if response.status_code != requests.codes.ok:
                raise Exception
        except Exception as e:
            raise SystemExit(e)

        for el in response.json()["categories"]["items"]:
            if (use_category_filter == True and el["id"] in category_filter) or use_category_filter == False:
                data["categories"].append({
                    "id": el["id"], 
                    "name": el["name"]
                })

    if write_to_file == True:
        with open(path_to_file, 'w') as outfile:
            json.dump(data, outfile, indent=2)

    return data