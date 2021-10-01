import requests
from dotenv import load_dotenv
import os
import json

load_dotenv('.env')


# Function: get features of track
def getFeatures(idList):
    url = "https://api.spotify.com/v1/audio-features?ids={}".format(idList)

    payload={}
    headers = {
    'Authorization': "Bearer " + os.environ.get('API_KEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

# Function: get songs of an album

def getTracksOfAlbum(albumID):
    url = "https://api.spotify.com/v1/albums/{}/tracks?market=DE&limit=30".format(albumID)

    payload={}
    headers = {
    'Authorization': "Bearer " + os.environ.get('API_KEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    items = resp['items']

    idList = ""
    
    for data in items:
        items_data = data
        song = items_data['name']
        uid = items_data['uri']
        id = items_data['id']
        idList += ('%2C' + id)
        print(song)
        print(id)

    getFeatures(idList[3: ])

# Function: get albums of an artist

def getAlbums(artistID):
    url = "https://api.spotify.com/v1/artists/{}/albums?market=DE&limit=20".format(artistID)

    payload={}
    headers = {
    'Authorization': "Bearer " + os.environ.get('API_KEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    items = resp['items']
    
    for data in items:
    
        items_data = data
        
        if items_data['album_group'] == 'album':
            album = items_data['name']
            uid = items_data['uri']
            id = uid[14 : ]
            print(album + ':')
            getTracksOfAlbum(id)
            print("-----")
            break
        
    print("------------")


# Function: get artist 

def getArtist(artist):

    url = "https://api.spotify.com/v1/search?q={}&type=artist&market=DE&limit=1".format(artist)

    payload={}
    headers = {
    'Authorization': "Bearer " + os.environ.get('API_KEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    resp = json.loads(response.text)

    artists = resp['artists']
    items = artists['items']

    for data in items:

        items_data = data
        artist = items_data['name']
        uid = items_data['uri']
        id = uid[15 : ]

        print(artist)
        print("------------")

        # call function
        getAlbums(id)



getArtist("Rin")