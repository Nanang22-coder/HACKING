import socket
import requests
import pprint
import json

hostname = input("enter a domain name :")
ip_address = socket.gethostbyname(hostname)
print(f"ip address =  {ip_address} \n \n")
url = "https://geolocation-db.com/jsonp/" + ip_address
response = requests.get(url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
  pprint.pprint(str(k) + ':' + str(v))
