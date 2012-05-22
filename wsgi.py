import os
import sys
import site

sys.path.append('/var/www/vhosts/alpha.publicspaceinvaders.org/')
sys.path.append('/var/www/vhosts/alpha.publicspaceinvaders.org/psi/')

from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'psi.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
