from django.conf.urls import patterns, include, url

urlpatterns = patterns('commProd.views',
	url(r'^processprod$', 'processProd'),
    url(r'^vote/(?P<type>\w+)$', 'vote'),
    url(r'^search$', 'search'),
    url(r'^api/search$', 'api_search'),
    url(r'^api/profile_data$', 'profile_data'),
    url(r'^(?P<username>.+)/(?P<cp_id>\d+)$', 'permalink'),
    url(r'^correction?', 'correction'),
    url(r'^$', 'home')
)