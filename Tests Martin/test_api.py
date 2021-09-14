import requests
import pprint

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer BQDk38ZbQcn1AdMjC4oisjiVYaTpuGWb5CwfDcLbeMzt9i-A584iKigiXMRFfnFSrTG0-_IYRsac-7eVwEfOVHZVWmWiTZ1UR_SV2bQxqGdVXeLTvw3FCOs1ujxWioZpOP9cJbeXwzYaM9a2x2SiJ4ZABsnl-JSzUQVZItLphM_IZU8BPw"
}
response = requests.get("https://api.spotify.com/v1/audio-features/1YI006fNvkEW0QiYQX54XL", headers=headers)

response.json()

pprint.pprint(response.json())