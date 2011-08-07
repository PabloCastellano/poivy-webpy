#!/usr/bin/env python

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
