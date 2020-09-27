#The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Danya.html
#this program is basic for how web crawler work

import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
#these three lines are not neccessary if the page is http.if it is https we need these lines
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#enter the starting url
url=input('Enter the url: ')
#Enter the number of time the crawler should follow the links
count=int(input('Enter count:'))
#enter the position of the next url to be followed from the current page
position=int(input('Enter position of url:'))

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retreiving: ',url)
    #since the first link in the page is stored as zeroth index in the tags list,so the position 3 on web page is
    #tags[2] in tags list.and tags[0] is the first link on the webpage.
    url=tags[position-1].get('href',None)
print('Retreiving: ',url)

