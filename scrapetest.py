from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://sofascore.com")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
