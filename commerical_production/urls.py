from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^bombers/', include('commerical_production.base_urls')),
    url(r'', include('commerical_production.base_urls'))
)