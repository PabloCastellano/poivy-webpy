#!/usr/bin/env python

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
