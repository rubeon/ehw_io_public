"""
This is the main site URL definitionself.

To map a path to a fuction, add it to the 'urlpatters' list below
"""


import xblog.urls
import haystack.urls

from django.urls import include, path, re_path
from django.contrib import admin
from django_xmlrpc.views import handle_xmlrpc
from .views import health
from django.conf import settings


urlpatterns = [
    path('accounts/', include(xblog.urls), name='profile'),
    # url(r'^accounts/', include(xblog.urls), name='profile'),
    path('admin/', admin.site.urls),
    path('xmlrpc/|mt-xmlrpc.cgi$|xmlrpc.php', handle_xmlrpc, name='xmlrpc'),
    path('search/', include(haystack.urls), name="search"),
    path('health', health),
    path('comments/', include('django_comments.urls'), name='comments'),
    path('blog/', include(xblog.urls)),
    #path('', include(social.apps.django_app.urls, namespace="social"), name='social'),
    path('', include('social_django.urls', namespace='social')),
    path('', include(xblog.urls, namespace='xblog')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)