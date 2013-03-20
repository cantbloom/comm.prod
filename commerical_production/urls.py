from django.conf.urls import patterns, include, url
from django.shortcuts import HttpResponse
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
	url(r'^public/(?P<path>.*)$', 'django.views.static.serve',
	 {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'^commprod/', include('commProd.urls')),
    url(r'^donations/', include('donations.urls')),
    url(r'^donate/', 'donations.views.donate'),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
)

urlpatterns += patterns('commerical_production.views',
    url(r'^googlead6c3c617c310b08.html$', 'google_verify'),


    url(r'^register/(?P<key>\w+)', 'register'),
    url(r'^confirm_email/(?P<key>\w+)', 'confirm_email'),
    url(r'^claim_email$', 'claim_email'),
    url(r'^users/(?P<username>.+)$', 'profile'),
    url(r'^edit$', 'edit_profile'),
    url(r'^welcome$', 'welcome'),
    url(r'^home$', 'home'),
    url(r'^feedback$', 'feedback'),
    url(r'^login$', 'login', {'template_name': 'login.html'}),
    url(r'^reset_password/(?P<key>\w+)', 'reset_password_confirm'),
    url(r'^reset_password', 'reset_password'),
    url(r'^$', 'home'),
)
