#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py - This file is part of poivy-webpy - 8/August/2011
# Copyright (C) 2011 Pablo Castellano <pablo@anche.no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__version__ = 1.0
__author__ = "Pablo Castellano <pablo@anche.no>"
__license__ = "GNU GPLv3+"


import web
import send

urls = (
	"/send", send.app_send,
	"/.*", "index"
)

app = web.application(urls, globals())

class index:
	def getCredit(self):
		import urllib, urllib2, cookielib
		import re
		import settings
		
		jar = cookielib.CookieJar()
		handler = urllib2.HTTPCookieProcessor(jar)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)

		params = urllib.urlencode({'user':settings.USERNAME, 'pass':settings.PASSWORD})

		urllib2.urlopen(settings.URL1, params)

		f = urllib2.urlopen(settings.URL2)

		ll = f.readlines()

		for l in ll:
			if "&euro;&nbsp;" in l:
				eur = l
			
		g3 = re.compile(".*&euro;&nbsp;([0-9\.]*)\s*")
		return g3.match(eur).group(1)

	def GET(self):
		render = web.template.render('templates')
		a = self.getCredit()
		return render.index(a)

if __name__ == "__main__":
    app.run()
