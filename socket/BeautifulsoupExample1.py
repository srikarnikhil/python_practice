#a Python program to use urllib to read the HTML from the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file
# http://py4e-data.dr-chuck.net/comments_42.html
#http://py4e-data.dr-chuck.net/comments_961265.html
import urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup

total=0
url=input('Enter the url to be scrapped: ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

spantags=soup('span')
for tag in spantags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    total=total+int(tag.contents[0])


print(total)
