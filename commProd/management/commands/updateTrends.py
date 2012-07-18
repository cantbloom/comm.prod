#! /usr/bin/env python

## crontab prefs
## * * * * * source /home/cantbloom/commprod/venv/bin/activate >/dev/null 2>&1; python /home/cantbloom/commprod/manage.py updateTrends >/dev/null 2>&1

from django.core.management.base import NoArgsCommand
from django.db.models import F
from commProd.models import CommProd


class Command(NoArgsCommand):
    help = 'Updates the trending score for all of the commprod objects'
    def handle(self, **options):
        self.stdout.write('Beginning update...\n')
        CommProd.objects.filter(trending_score__gt=0).update(trending_score = F('trending_score') - 1)
        CommProd.objects.filter(trending_score__lt=0).update(trending_score = 0 )

        self.stdout.write('Update complete.\n')