import requests
import http
from dotenv import load_dotenv
import sys
import os
import json
from authentication import *
import math
from categories import getAllCategories
from playlists import getPlaylistsForCategories
from http_setup import setupRequestsSession
from tracks import getTracksOfPlaylists
import pandas as pd


#Get environment variables from ".env" file and read credentials
load_dotenv('.env')
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

#Get auth token
auth_token = getAuthTokenFromCredentials(client_id, client_secret)

http = setupRequestsSession()

data = {}

#To load data_object from file instead of rerunning the scripts, do:
file = open(os.path.join("data_collection", "json", "playlists.json"))
data = json.load(file)

#data = getAllCategories(http, auth_token, data,True, os.path.join("data_collection", "json", "categories.json"))
#getPlaylistsForCategories(http, auth_token, data,True, os.path.join("data_collection", "json", "playlists.json"))
data = getTracksOfPlaylists(http, auth_token, data,True, os.path.join("data_collection", "json", "tracks.json"))