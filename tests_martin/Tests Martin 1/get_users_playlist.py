import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv('.env')

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.environ.get('API_KEY')
}
response = requests.get("https://api.spotify.com/v1/me/playlists?limit=10&offset=5", headers=headers)

response.json()

pprint.pprint(response.json())
