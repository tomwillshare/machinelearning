import requests
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.tomwillshare.com/Machine%20Learning/"

r = requests.get(url)

html_content = r.text

soup = BeautifulSoup(html_content, "html.parser")

for tr in soup.find_all('tr')[2]:
  tds = soup.find_all('td')
  print("value: %s,value2: %s,value3: %s\n" %\
  (tds[0].text, tds[1].text, tds[2].text))
