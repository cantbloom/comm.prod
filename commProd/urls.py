from django.conf.urls import patterns, include, url

urlpatterns = patterns('commProd.views',
	url(r'^register/(?P<key>\w+)', 'register'),
	url(r'^processprod$', 'processProd'),
    url(r'^users/(?P<user_id>\d+)$', 'profile'),
    url(r'^users/(?P<username>\w+)$', 'profile'),
    url(r'^users/(?P<alt_email>\w+@\w+(?:\.\w+))$', 'profile'),
    url(r'^vote$', 'vote'),
    url(r'^get_users$', 'get_users'),
    url(r'^home$', 'home'),
    url(r'^popular$', 'search', 
        {
        'title':'Popular comm.prods', 
        'nav' : ('nav_home',' active'),
        'subnav' : ('subnav_popular', 'active'),
        'orderBy': 'avg_score', 
        'direction': 'lh'
        }),
    url(r'^recent$', 'search', 
        {
        'title':'Recent comm.prods',
        'nav' : ('nav_home',' active'),
        'subnav' : ('subnav_recent', 'active'),
        'orderBy': 'date', 
        'direction':'lh',
        }),
    url(r'^$', 'home'),
)