from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
	url(r'^public/(?P<path>.*)$', 'django.views.static.serve',
	 {'document_root': settings.MEDIA_ROOT}),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'^commprod/', include('commProd.urls')),
)

urlpatterns += patterns('commerical_production.views',
    url(r'^register/(?P<key>\w+)', 'register'),
    url(r'^confirm_email/(?P<key>\w+)', 'confirm_email'),
    url(r'^claim_email$', 'claim_email'),
    url(r'^users/(?P<username>.+)$', 'profile'),
    url(r'^welcome$', 'welcome'),
    url(r'^home$', 'home'),
    url(r'^feedback$', 'feedback'),
    url(r'^$', 'home'),
)