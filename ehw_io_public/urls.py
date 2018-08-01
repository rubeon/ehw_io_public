"""
This is the main site URL definitionself.

To map a path to a fuction, add it to the 'urlpatters' list below
"""


import xblog.urls
import social.apps.django_app.urls
import haystack.urls

from django.conf.urls import include, url
from django.contrib import admin
from django_xmlrpc.views import handle_xmlrpc
from .views import health

urlpatterns = [
    # Examples:
    url(r'^accounts/', include(xblog.urls), name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xmlrpc/$|^mt-xmlrpc.cgi$|^xmlrpc.php$', handle_xmlrpc, name='xmlrpc'),
    url(r'^search/', include(haystack.urls), name="search"),
    url(r'health$', health),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^blog/', include(xblog.urls)),
    url('', include(social.apps.django_app.urls, namespace="social"), name='social'),
    url(r'', include(xblog.urls, namespace='xblog')),
]

