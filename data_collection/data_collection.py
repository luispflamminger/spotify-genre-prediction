import http
from dotenv import load_dotenv
import os
import json
from functions.authentication import *
from functions.categories import getAllCategories
from functions.playlists import getPlaylistsForCategories
from functions.http_setup import setupRequestsSession
from functions.features import getFeaturesOfTracks
from functions.tracks import getTracksOfPlaylists
from functions.flatten_json import flattenJSON


#Get environment variables from ".env" file and read credentials
load_dotenv('.env')
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

#Get auth token
auth_token = getAuthTokenFromCredentials(client_id, client_secret)

http = setupRequestsSession()

data = {}

#Filter for which category ids should be used
#category_filter = ["hiphop", "rock", "jazz"]

#To load data_object from file instead of rerunning the scripts, do:
file = open(os.path.join("data_collection", "json", "tracks_full.json"))
data = json.load(file)

# data = getAllCategories(http, auth_token, data, False, None, True, os.path.join("data_collection", "json", "categories_full.json"))
# print("got categories")
# data = getPlaylistsForCategories(http, auth_token, data, True, os.path.join("data_collection", "json", "playlists_full.json"))
# print("got playlists")
# data = getTracksOfPlaylists(http, auth_token, data, True, os.path.join("data_collection", "json", "tracks_full.json"))
# print("got tracks")
# data = getFeaturesOfTracks(http, auth_token, data, True, os.path.join("data_collection", "json", "features_full.json"))
# print("got features")

#Flatten JSON
print("starting to flatten json")
flattenJSON(data, True,  os.path.join("data_collection", "json", "flat_json_no_features.json"))
print("done")