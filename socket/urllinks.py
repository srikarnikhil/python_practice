#finding all the url links available in a web page using beautifulSoup library

import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup

html=urllib.request.urlopen('http://www.dr-chuck.com/page2.htm').read()
soup=BeautifulSoup(html,'html.parser    ')

#retreive all of anchor tags

tags=soup('a')
for tag in tags:
    print(tag.get('href',None))


