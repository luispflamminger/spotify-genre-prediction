import requests
from dotenv import load_dotenv
import os
import json

load_dotenv('.env')

url = "https://api.spotify.com/v1/search?q=Rin&type=artist&market=DE&limit=1"

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
  print(uid)
  print(id)