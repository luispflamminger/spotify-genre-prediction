import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

url = "https://api.spotify.com/v1/albums/7FzVARL5hF1iZPpOTCyMpp/tracks?market=DE&limit=30"

payload={}
headers = {
  'Authorization': "Bearer " + os.environ.get('API_KEY')
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)