from django.conf.urls import patterns, include, url

urlpatterns = patterns('commProd.views',
	url(r'^register/(?P<key>\w+)/', 'register'),
		url(r'^processprod$', 'processProd'),
    url(r'^users/(?P<user_id>\d+)/$', 'profile'),
    url(r'^users/(?P<username>\w+)/$', 'profile'),
    url(r'^home$', 'home'),
    url(r'^$', 'home')
)
