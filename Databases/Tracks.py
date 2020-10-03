import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('trackdb.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE 
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

fname=input('Enter the file name :')
if len(fname)<1:fname='Library.xml'


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
#if we pass a key to this function,it's value is returned.eg:if we pass Artist ,Queen will be returned.if we pass Track ID,369 will be returned.
def lookup(d,key):
    found=False
    for child in d:
        if found:return child.text
        if child.tag=='key' and child.text==key:
            found=True

    return None




stuff=ET.parse(fname)
allentries=stuff.findall('dict/dict/dict')
print('Dict count: ',len(allentries))

for entry in allentries:
    if lookup(entry,'Track ID') is None:continue

    name=lookup(entry,'Name')
    artist=lookup(entry,'Artist')
    album=lookup(entry,'Album')
    count=lookup(entry,'Play Count')
    rating=lookup(entry,'Rating')
    length=lookup(entry,'Total Time')

    if name is None or artist is None or album is None:
        continue


    print(album,rating)

    cur.execute('INSERT OR IGNORE INTO Artist(name) values (?)',(artist,))
    cur.execute('SELECT id from Artist where name=?',(artist,))
    artist_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album(title,artist_id) values (?,?)', (album,artist_id))
    cur.execute('SELECT id from Album where title=?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Track(title,album_id,len,rating,count) values (?,?,?,?,?)', (name, album_id,length,rating,count))
    conn.commit()



