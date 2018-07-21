import xblog.urls
import social.apps.django_app.urls
import haystack.urls

from django.conf import settings
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
    url('', include(social.apps.django_app.urls, namespace="social"), name='social'),
    url(r'', include(xblog.urls, namespace="xblog")),
]

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))
#
# urlpatterns +=    patterns('', url(r'^$', include('xblog.urls')),)
