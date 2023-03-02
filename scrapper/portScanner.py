import socket

def scan(ipaddress,port):
  s = socket.socket()
  rc = s.recv(1024)
  rc = rc.decode("utf-8")
  s.connect((ipaddress,port))
  print(f'{str(port)} is active', rc)
  
ip  = input("masukan ip address")
port = input("masukan port")

if "-" in port:
  p = port.split("-")
  for x in range(int(p[0]),int(p[1])):
    scan(ip,x)
