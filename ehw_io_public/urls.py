from django.conf import settings 
from django.conf.urls import patterns, include, url
from django.contrib import admin
import xblog.urls
import social.apps.django_app.urls
import haystack.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ehw_io_public.views.home', name='home'),
    url(r'^accounts/', include(xblog.urls), name='profile'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(xblog.urls), name='blog'),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),
    url(r'^xmlrpc.php$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),
    url(r'^mt-xmlrpc.cgi$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),
    url('', include(social.apps.django_app.urls), name='social'),
    url(r'^search/', include(haystack.urls), name="search"),
    # url(r"^$", TemplateView.as_view(template_name='base.html')),
    url(r'^$', include(xblog.urls)),

)

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))
# 
# urlpatterns +=    patterns('', url(r'^$', include('xblog.urls')),)

