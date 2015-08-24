#! /usr/bin/env python

import urllib2
import lxml.html
from lxml.cssselect import CSSSelector

response = urllib2.urlopen('https://www.ptt.cc/bbs/HardwareSale/index.html')
content = response.read()

root = lxml.html.fromstring(content)

#print lxml.html.tostring(root)

sel = CSSSelector('div.pull-right')

results = sel(root)
#print results

match = results[0]
print lxml.html.tostring(match)

