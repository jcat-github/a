import requests as bruh
import json
api = json.loads(bruh.get("https://randomuser.me/api").text)
name = api['results'][0]['name']['title']+" "+api['results'][0]['name']['first']
print(name)
import urllib.request

image_url = api['results'][0]['picture']['large']

urllib.request.urlretrieve(image_url, 'images/local_image.jpg')
from flask import Flask
app = Flask('app', static_folder="images/")

@app.route('/')
def hello_world():
  return f'<img src="{image_url}"> <h2>{name}</h2>'

app.run(host='0.0.0.0', port=8080)

