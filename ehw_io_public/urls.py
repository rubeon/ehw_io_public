import xblog.urls
import social.apps.django_app.urls
import haystack.urls

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django_xmlrpc.views import handle_xmlrpc

urlpatterns = [
    url(r'^accounts/', include(xblog.urls), name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xmlrpc/$|^mt-xmlrpc.cgi$|^xmlrpc.php$', handle_xmlrpc, name='xmlrpc'),
    url(r'^search/', include(haystack.urls), name="search"),
    url('', include(social.apps.django_app.urls, namespace="social"), name='social'),
    url(r'', include(xblog.urls, namespace="xblog")),
]

