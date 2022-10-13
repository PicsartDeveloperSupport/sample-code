import os
import requests
import json
from requests_toolbelt.multipart import encoder

picsartURL = 'https://api.picsart.io/tools/1.0/removebg'
imageFile = '<path to file>'

headers = {'accept':'application/json', 'apikey': '<your api key>'}

payload = {'output_type':'cutout', 'format':'jpeg'}

files = {
    'json': (None, json.dumps(payload), 'application/json'),
    'image': (os.path.basename(imageFile), open(imageFile, 'rb'), 'application/octet-stream')
}

response = requests.post('https://api.picsart.io/tools/1.0/removebg', headers=headers, files=files)

print (response.status_code)

print (response.text)