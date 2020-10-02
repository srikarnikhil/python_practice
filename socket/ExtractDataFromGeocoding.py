#Extracting data from google geocoding api
#example address(location):Ann Arbor,MI
#Google maps api
import urllib.request,urllib.parse
import json

#url of api exposed by google to get data
serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input('Enter Location: ')
    if len(address)<1:break
    #urlencode encode the data like making space to + and comma(,) to % etc
    url=serviceurl+urllib.parse.urlencode({'address':address})
    print('Retrieving :'+url)
    urlhandle=urllib.request.urlopen(url)
    #decodes data from utf-8 to unicode
    data=urlhandle.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        #this will change json data to python dictionary format
        js=json.loads(data)
    except:
        #if the json data is not valid syntax it will blow up
        js=None

    if not js or 'status' not in js or js['status']!='OK':
        print('===Failed to retrieve data===')
        print(data)
        continue
    print(json.dumps(js,indent=4))
    #since js in python dictionary,the keys can be accessed to get data
    latitude=js['results'][0]['geometry']['location']['lat']
    longitude=js['results'][0]['geometry']['location']['lon']

    print('latitude: ',latitude,' longitude',longitude)
    location=js['results'][0]['formatted_address']
    print(location)