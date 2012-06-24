from django.conf.urls.defaults import *
from cloudmailin.views import MailHandler



urlpatterns = patterns('',
    url(r'^mail/$', mail_handler),
)