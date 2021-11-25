# -*- coding: utf-8 -*-
"""
	Thor Add-on
"""

from resources.lib.modules.control import addonPath, addonId, getThorVersion, joinPath
from resources.lib.windows.textviewer import TextViewerXML


def get(file):
	thor_path = addonPath(addonId())
	thor_version = getThorVersion()
	helpFile = joinPath(thor_path, 'resources', 'help', file + '.txt')
	f = open(helpFile, 'r', encoding='utf-8', errors='ignore')
	text = f.read()
	f.close()
	heading = '[B]Thor -  v%s - %s[/B]' % (thor_version, file)
	windows = TextViewerXML('textviewer.xml', thor_path, heading=heading, text=text)
	windows.run()
	del windows