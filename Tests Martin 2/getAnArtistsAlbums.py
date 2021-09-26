import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

url = "https://api.spotify.com/v1/artists/18ISxWwWjV6rPLoVCXf1dz/albums?market=DE&limit=20"

payload={}
headers = {
  'Authorization': "Bearer " + os.environ.get('API_KEY')
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
