import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

#url = "https://api.spotify.com/v1/audio-features?ids=034jxfixe0Gogd6p0reMnP%2C4Y5ShamuGjxfQWdwY1Kz5R"
url = "https://api.spotify.com/v1/audio-features?ids=034jxfixe0Gogd6p0reMnP%4Y5ShamuGjxfQWdwY1Kz5R"


payload={}
headers = {
  'Authorization': "Bearer " + os.environ.get('API_KEY')
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)