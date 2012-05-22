#def application(environ, start_response):
#	status = '200 OK'
#	output = 'Hello World!'
#
#	response_headers = [('Content-type', 'text/plain'),
#				('Content-Length', str(len(output)))]
#
#	start_response(status, response_headers)
#
#	return [output]

import os
import sys

sys.path.append('/var/www/vhosts/alpha.publicspaceinvaders.org/psi/')
sys.path.append('/var/www/vhosts/alpha.publicspaceinvaders.org/')

from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
