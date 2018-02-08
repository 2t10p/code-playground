#!/usr/bin/env python
# -*- coding: utf-8 -*

import urllib2
import HTMLParser
import lxml.html
from lxml.cssselect import CSSSelector
from bs4 import BeautifulSoup

url = "https://statsroyale.com/tournaments"
request_headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

request = urllib2.Request(url, headers=request_headers)
contents = urllib2.urlopen(request).read()

root = lxml.html.fromstring(contents)
sel = CSSSelector('div .challenges__rowContainer')
results = sel(root)

htmlParser = HTMLParser.HTMLParser()
for result in results:
    trimContent = lxml.html.tostring(result).strip(' \t\n\r')
    soup=BeautifulSoup(trimContent, 'lxml')
    text = soup.get_text(" | ", strip=True)
    infos = text.split(" | ")
    infos.pop(1)
    infos.pop(-1)
    infos.pop(-1)
    infos.pop(-1)

    players = infos[1]
    if players != "50/50":
        print ' | '.join(infos).encode('utf-8').strip()


