# -*- coding: utf-8 -*-
"""
	Thor Add-on
"""

try: #PY2
	from urllib.request import urlopen, Request
except ImportError: # PY3
	from urllib2 import urlopen, Request
from resources.lib.modules.control import addonPath, addonId, joinPath
from resources.lib.windows.textviewer import TextViewerXML

thor_path = addonPath(addonId())
news_file = 'https://raw.githubusercontent.com/aussiehulk/zips/master/plugin.video.thor/newsinfo.txt'
local_news = joinPath(thor_path, 'newsinfo.txt')


def news():
	message = open_news_url(news_file)
	compfile = open(local_news).read()
	if len(message) > 1:
		if compfile == message: pass
		else:
			text_file = open(local_news, "wb")
			text_file.write(message)
			text_file.close()
			compfile = message
	showText('[B]News and Info[/B]', compfile)

def open_news_url(url):
	req = Request(url)
	req.add_header('User-Agent', 'klopp')
	response = urlopen(req)
	link = response.read()
	response.close()
	return link

def news_local():
	compfile = open(local_news).read()
	showText('[B]News and Info[/B]', compfile)

def showText(heading, text):
	windows = TextViewerXML('textviewer.xml', thor_path, heading=heading, text=text)
	windows.run()
	del windows