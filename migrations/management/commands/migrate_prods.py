
from django.core.management.base import NoArgsCommand
from commProd.models import *

from datetime import datetime, timedelta
from os import environ as env

import requests, time, simplejson as json

class Command(NoArgsCommand):
    help = 'Migrates prods from dev to production from the prod dump from Chris Post'
    def handle(self, **options):
        day_zero = datetime(2009, 9, 4, 13, 59, 12) # first commprod from colin
        dump_day = datetime(2012, 8, 7, 0, 3, 29, 334728) # day before dump from post
        url = env['POST_URL_DUMP']
        commprods = CommProd.objects.filter(date_added__gt=dump_day, date__lt=day_zero).select_related()
        self.stdout.write("Starting...\n")
        for commprod in commprods:
            self.stdout.write("\nAdding %s" % str(commprod.id))
            data = json.dumps({
                        commprod.user_profile.user.email : (
                            commprod.email_content.content,
                            [commprod.content], 
                            commprod.date.isoformat(),
                            commprod.email_content.subject,
                            )
                        })
            r = requests.post(url, data={'data' : data, 'key' : env['SECRET_KEY']})
            time.sleep(0.5) # don't overload poor heroku
            self.stdout.write(r.text + "\n")
        self.stdout.write("Done.\n")
