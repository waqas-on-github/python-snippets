import requests
import json
data=requests.get('https://api.github.com/events')
d=data.json()


with open('data.Json' ,'w' ,encoding='utf-8') as j:
    j.write(json.dumps(d))

