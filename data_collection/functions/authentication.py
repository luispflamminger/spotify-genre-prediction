import requests

# Authenticate and get an API Token from Spotify using a Client ID and secret
# requires requests import
def getAuthTokenFromCredentials(id, secret):

    url = "https://accounts.spotify.com/api/token"

    payload = f'grant_type=client_credentials&client_id={id}&client_secret={secret}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()["access_token"]
