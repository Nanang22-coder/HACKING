from collections import deque
import re

from bs4 import BeautifulSoup
import requests
import urllib.parse

user_url = str(input('[+] masukan url:  '))
limit = int(input('[+] masukan limit: '))
urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0

try:
  while True:
    count += 1
    if count > limit:
      break
    url = urls.popleft() # ambil paling kiri
    scraped_urls.add(url)
    parts = urllib.parse.urlsplit(url)
    base_url = f"{parts.scheme}://{parts.netloc}"
    path = url[:url.rfind("/")+1] if "/" in parts.path else url
    print(f"{count} Memproses {url}")
    try:
      response = requests.get(url)
    except(requests.exceptions.MissingScema, requests.exceptions.ConnectionError):
      continue
    new_email = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.+[a-z\.]+',response.text,re.I))
    emails.update(new_email)
    soup = BeautifulSoup(response.text, 'html.parser')
    for anchor in soup.find_all('a'):
      link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
      if link.startswith("/"):
        link = base_url + link
      elif not link.startswith('http'):
        link = path + link
      if not link in urls and not link in scraped_urls:
        urls.append(link)
    
except keyboardInterrupt:
  print('[-] closing.!')

print('\n Proses Selesai')
print(f'\n {len(emails)} email di temukan \n --------')
for mail in emails:
  print(' ' + mail)
  print('\n ')
