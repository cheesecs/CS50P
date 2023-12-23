import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

resp = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
o = resp.json()
for result in o["results"]:
    print(result["trackName"])