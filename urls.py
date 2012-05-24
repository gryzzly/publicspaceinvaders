import os
from settings import * 
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'psi.invaders.views.data', name='data'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root':  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'media')
    }),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
      'document_root':  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
    }),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
