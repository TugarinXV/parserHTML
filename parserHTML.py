import requests as rq
from bs4 import BeautifulSoup

url = str(input("enter link: "))
if 'https' in url or 'http' in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, 'html.parser')
links = []
for link in soup.find_all('a'):
    links.append(link.get("href"))
with open('myLinks.txt', 'a') as saved:
    for link in links:
        print(link, file=saved)
