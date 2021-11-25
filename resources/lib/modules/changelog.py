# -*- coding: utf-8 -*-
"""
	Thor Add-on
"""

from resources.lib.modules.control import addonPath, addonId, getThorVersion, joinPath
from resources.lib.windows.textviewer import TextViewerXML


def get():
	thor_path = addonPath(addonId())
	thor_version = getThorVersion()
	changelogfile = joinPath(thor_path, 'changelog.txt')
	r = open(changelogfile)
	text = r.read()
	r.close()
	heading = '[B]Thor -  v%s - ChangeLog[/B]' % thor_version
	windows = TextViewerXML('textviewer.xml', thor_path, heading=heading, text=text)
	windows.run()
	del windows