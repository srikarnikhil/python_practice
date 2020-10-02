import urllib.request,urllib.parse
import json

#: http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_961268.json

url=input('Enter the url to fetch data : ')
jsondata=urllib.request.urlopen(url).read()
print('Retrieving...',url)
#this loads method takes json string as in put ah convert to json dictionary so that accessing the keys is easier
js=json.loads(jsondata)
total=0
count=0
for comment in js['comments']:
    count=count+1
    total=total+int(comment['count'])

print('Count :',count)
print('sum:',total)