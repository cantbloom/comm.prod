from django.conf.urls import patterns, url

from runner import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'runs/(?P<run_id>\d+)$', views.index),
    url(r'sort/(?P<sortby>\w+)', views.index),
    url(r'api/all_drinks$', views.get_all_drinks),
    url(r'api/get_order/(?P<run_id>\d+)$', views.get_order),
    url(r'api/update_run/(?P<run_id>\d+)$', views.update_run),
)
