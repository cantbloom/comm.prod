from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin', include(admin.site.urls)),
	url(r'^public/(?P<path>.*)$', 'django.views.static.serve',
	 {'document_root': settings.MEDIA_ROOT}),
    url(r'^login$', 'django.contrib.auth.views.login',
     {'template_name': 'login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout',
    	{'template_name': 'logout.html'}),

    url(r'', include('commProd.urls')),
)
