#!/usr/bin/env python
# -*- coding: utf-8 -*-
# send.py - This file is part of poivy-webpy - 8/August/2011
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

urls = (
  "", "sendSMS"
)

class sendSMS:
    def GET(self):
	return "You must use a POST request"

    def POST(self):
	import urllib, urllib2, cookielib
	import re
	import settings
	
	jar = cookielib.CookieJar()
	handler = urllib2.HTTPCookieProcessor(jar)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)

	x = web.input()
	
	params = urllib.urlencode({'user':settings.USERNAME, 'pass':settings.PASSWORD})
	params2 = urllib.urlencode({'action':'send', 'panel': 'true', 'message':x['text'], 'callerid':settings.CALLERID, 'bnrphonenumber':x['number'], 'sendscheduled': 'no'})

	urllib2.urlopen(settings.URL1, params)
	urllib2.urlopen(settings.URL2)
	urllib2.urlopen(settings.URL3, params2)

	render = web.template.render('templates')
	return render.send()

app_send = web.application(urls, locals())
