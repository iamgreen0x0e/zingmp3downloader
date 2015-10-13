import sys
import os
import re
import argparse
from unidecode import unidecode
import unicodedata
import urllib
from StringIO import StringIO
import gzip
import BeautifulSoup

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse


def getContent(url):
	try:
		request = urllib2.Request(url);
		request.add_header('Accept-encoding','gzip')
		response = urllib2.urlopen(request)
		if response.info().get('Content-Encoding') == 'gzip':
			buf = StringIO(response.read())
			f = gzip.GzipFile(fileobj = buf)
			data = f.read()
		else:
			data = response.read()
		return data
	except  Exception, e:
		return e


url = raw_input("enter link: ")
pattern = re.compile(r'http://mp3\.zing\.vn/xml/album-xml/.\w+')
data = getContent(url)
matches =  pattern.findall(data)
# if matches is None:
# 	print "null nhe"
# else:	

album_data = getContent(matches[0])
# album_data = re.sub(r'\n', '', album_data)
# print album_data
#working with folder;
# album_content = BeautifulSoup.BeautifulSoup(album_data)
# all_album = album_content.findAll('item')
# for item in all_album:
# 	song_name = re.search(r'<title><!\[CDATA\[(.*)]]></title>', item)
# 	song_name = song_name.group(1)
# 	source = re.search(r'<source><!\[CDATA\[(.*)]]></source>', item)
# 	source = song_name.group(1)
# 	print (song_name,'...',source)

item_pattern = re.compile(r'<item type="mp3">(.*?)</item>',re.M)
all_album = item_pattern.findall(album_data)
print all_album
# i=1
# for item in all_album:
# 	# song_name = re.search(r'<title><!\[CDATA\[(.*)\]\]></title>', item)
# 	# song_name = song_name.group(1)
# 	# source = re.search(r'<source><!\[CDATA\[(.*)\]\]></source>', item)
# 	# source = source.group(1)
# 	# print (song_name,'___',source)
# 	# break
# 	i+=1

# print i