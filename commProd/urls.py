from django.conf.urls import patterns, include, url

urlpatterns = patterns('commProd.views',
	url(r'^register/(?P<key>\w+)/', 'register'),
		url(r'^processprod$', 'processMail'),
    url(r'^users/(?P<user_id>\d+)/$', 'user'),
    url(r'^$', 'home')
)
