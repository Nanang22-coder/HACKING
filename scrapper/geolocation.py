import socket
import requests
import pprint
import json


ip = input("masukan ip ip_address :   ")

url = "https://geolocation-db.com/jsonp/" + ip
response = requests.get(url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
  pprint.pprint(str(k) + ':' + str(v))


