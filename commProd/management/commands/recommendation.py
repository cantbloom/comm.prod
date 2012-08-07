#! /usr/bin/env python

from django.core.management.base import NoArgsCommand
from commProd.models import UserProfile, CommProdRec, CommProd

from datetime import date, datetime, timedelta


class Command(NoArgsCommand):
    help = 'Updates commprod recommnedation list for each user'

    def handle(self, **options):
        print "Making CommProdRecs"
        commprods = CommProd.objects.all();

        active_users = UserProfile.objects.filter(user__is_active = True)

        to_add = []

        for user_profile in active_users:
            print user_profile.user.username
            for commprod in commprods:
                rec = CommProdRec(user_profile = user_profile, commprod = commprod)
                rec.update_scores()
                to_add.append(rec)
                print rec.weighted_avg, rec.time_period*5.0, rec.like_author/3.0 , rec.author_popularity/10.0 , rec.commprod.trending_score/500.0 , rec.commprod.score*1.0

        CommProdRec.objects.bulk_create(to_add)
        print "Complete"

