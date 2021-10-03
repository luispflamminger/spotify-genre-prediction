import requests
from dotenv import load_dotenv
import os
import json
import xlsxwriter

load_dotenv('.env')


# Function: get features of track
def getFeatures(idList):
    url = "https://api.spotify.com/v1/audio-features?ids={}".format(idList)

    payload={}
    headers = {
    'Authorization': "Bearer " + os.environ.get('API_KEY')
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.text)

    resp = json.loads(response.text)

    audio = resp['audio_features']

    w, h = 18, 25
    audio_array = [[0 for x in range(w)] for y in range(h)] 

    rows    = 0
    columns = 0
    for data in audio:

        #audio_array.append(rows)
        #dataJSON = data.json.loads(data)
        items_data = data
        columns = 0

        for attribute, value in items_data.items():
                print(value)
                audio_array[rows][columns] = value
                columns += 1

        for it in items_data:
            print(it)
        
        rows += 1

    print("___")
    print(rows)
    print(columns)
    print(audio_array)


    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Track_Features - Test2.xlsx')
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, type, id, uri, track_href, analysis_url, duration_ms, time_signature in (audio_array):
        worksheet.write(row, col,     danceability)
        worksheet.write(row, col + 1, energy)
        worksheet.write(row, col + 2, key)
        worksheet.write(row, col + 3, loudness)
        worksheet.write(row, col + 4, mode)
        worksheet.write(row, col + 5, speechiness)
        worksheet.write(row, col + 6, acousticness)
        worksheet.write(row, col + 7, instrumentalness)
        worksheet.write(row, col + 8, liveness)
        worksheet.write(row, col + 9, valence)
        worksheet.write(row, col + 10, tempo)
        worksheet.write(row, col + 11, type)
        worksheet.write(row, col + 12, id)
        worksheet.write(row, col + 13, uri)
        worksheet.write(row, col + 14, track_href)
        worksheet.write(row, col + 15, analysis_url)
        worksheet.write(row, col + 16, duration_ms)
        worksheet.write(row, col + 17, time_signature)

        row += 1
        

    workbook.close()

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