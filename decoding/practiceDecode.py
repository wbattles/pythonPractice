#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#http://py4e-data.dr-chuck.net/comments_42.xml
#http://data.pr4e.org/romeo.txt

import urllib.request
import urllib.parse
import urllib.error

lnk = input('Enter location: ')
web = urllib.request.urlopen(lnk).read()

st = web.decode()

name = input('Enter txt name: ')
with open(name, 'w') as tx:
    tx.write(st)


# .decode() returns a string
#unicode turns it readable information
#also allows the links to save as their respective file types
#w/ formating in tact


# .read() only returns bytes
#the computer can use the data
#print() works, but it has b' '
#data hasnt been translated to unicode, so it does not export correctly