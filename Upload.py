import os
import requests
import json
from requests_toolbelt.multipart import encoder

picsartURL = 'https://api.picsart.io/tools/1.0/upload'
imageFile = '<path to file>'

headers = {
    'accept':'application/json',
    'apikey': '<your api key>'
}

payload = {}

files = {
    'json': (None, json.dumps(payload), 'application/json'),
    'image': (os.path.basename(imageFile), open(imageFile, 'rb'), 'application/octet-stream')
}

response = requests.post(picsartURL, headers=headers, files=files)

print (response.status_code)

print (response.text)
