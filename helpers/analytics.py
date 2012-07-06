#! /usr/bin/env python

## crontab prefs
## * * * * * /path/to/update_trending_score.py >/dev/null 2>&1  

from django.db.models import F
from commProd.models import CommProd

def update_trending_score():
	CommProd.objects.filter(trending_score__gt=0).update(trending_score = F('trending_score') - 1)
	CommProd.objects.filter(trending_score__lt=0).update(trending_score = 0 )
