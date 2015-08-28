#! /usr/bin/env python

import re
import HTMLParser
import urllib2
import lxml.html
from lxml.cssselect import CSSSelector

response = urllib2.urlopen('https://www.ptt.cc/bbs/HardwareSale/index.html')
content = response.read()

root = lxml.html.fromstring(content)
sel = CSSSelector('div .r-ent a')
#sel = CSSSelector('div.pull-right')

results = sel(root)

#match = results[0]
#print lxml.html.tostring(match)

htmlParser = HTMLParser.HTMLParser()
for result in results:
    trimContent = lxml.html.tostring(result).strip(' \t\n\r')
    decodeContent = htmlParser.unescape(trimContent)
    grepContent = re.search('<a href="/bbs(.+).html">(.+)</a>', decodeContent)

    #Get URL and Title
    grepContent.group(2)
    grepContent.group(1)


# get article
response = urllib2.urlopen('https://www.ptt.cc/bbs/HardwareSale/M.1440764830.A.212.html')
content = response.read()

root = lxml.html.fromstring(content)
sel = CSSSelector('#main-container')
results = sel(root)

htmlParser = HTMLParser.HTMLParser()
for result in results:
    trimContent = lxml.html.tostring(result).strip(' \t\n\r')
    decodeContent = htmlParser.unescape(trimContent).encode('utf-8')
    print decodeContent
