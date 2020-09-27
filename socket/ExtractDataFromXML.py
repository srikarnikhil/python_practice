
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and
# extract the comment counts from the XML data, compute the sum of the numbers in the file.
#http://py4e-data.dr-chuck.net/comments_961267.xml
#http://py4e-data.dr-chuck.net/comments_42.xml
import urllib.request,urllib.parse
import xml.etree.ElementTree as ET

url=input('Enter the url:')
xml=urllib.request.urlopen(url).read()
print('Retrieiving: ',url)

#reads the xml and stores it in the tree format
CommentsInfoTree=ET.fromstring(xml)
#all the comment tags under the comments tag are store in a list as list of trees
commentNodeList=CommentsInfoTree.findall('comments/comment')
totalsum=0
count=0
for comment in commentNodeList:
    count=count+1
    totalsum= totalsum + int(comment.find('count').text)

print('Count :',count)
print('sum:',totalsum)