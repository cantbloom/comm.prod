from django.conf.urls import patterns, include, url

urlpatterns = patterns('commProd.views',
	url(r'^processprod/$', 'mail_handler'),
    url(r'^users/(?P<user_id>\d+)/$', 'user'),
    url(r'^$', 'home')
)
