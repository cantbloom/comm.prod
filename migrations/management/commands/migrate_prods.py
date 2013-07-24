from django.core.management.base import NoArgsCommand
import commProd.models as cpm

from datetime import datetime
from os import environ as env

import simplejson as json
import requests
import time

class Command(NoArgsCommand):
    help = """Migrates prods from dev to production 
    from the prod dump from Chris Post"""
    def handle(self, **options):
        # first commprod from colin
        day_zero = datetime(2009, 9, 4, 13, 59, 12)
        # day before dump from post
        dump_day = datetime(2012, 8, 7, 0, 3, 29, 334728)
        url = env['POST_URL_DUMP']
        commprods = cpm.CommProd.objects.filter(
            date_added__gt=dump_day, 
            date__lt=day_zero).select_related()
        
        self.stdout.write("Starting...\n")
        
        for commprod in commprods.iterator():
            self.stdout.write("\nAdding %d" % commprod.id)
            data = json.dumps({
                        commprod.user_profile.user.email : (
                            commprod.email_content.content,
                            [commprod.content], 
                            commprod.date.isoformat(),
                            commprod.email_content.subject,
                            )
                        })
            r = requests.post(url, data={
                'data' : data, 
                'key' : env['SECRET_KEY']
            })
            # don't overload poor heroku
            time.sleep(0.5) 
            self.stdout.write("%s\n" % r.text)
        self.stdout.write("Done.\n")
