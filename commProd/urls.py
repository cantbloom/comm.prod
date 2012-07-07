from django.conf.urls import patterns, include, url

urlpatterns = patterns('commProd.views',
	url(r'^processprod$', 'processProd'),
    url(r'^vote$', 'vote'),
    url(r'^search$', 'search'),
    url(r'^api/search$', 'api_search'),
    #url(r'^api/vs_data$', 'vs_data'),
    url(r'^api/profile_data$', 'profile_data'),
    url(r'^$', 'home')
)