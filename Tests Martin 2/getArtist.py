import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

url = "https://api.spotify.com/v1/search?q=Rin&type=artist&market=DE&limit=1"

payload={}
headers = {
  'Authorization': "Bearer " + os.environ.get('API_KEY')
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)