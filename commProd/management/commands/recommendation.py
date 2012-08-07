#! /usr/bin/env python

from django.core.management.base import NoArgsCommand
from commProd.models import UserProfile, CommProdRec, CommProd

class Command(NoArgsCommand):
    help = 'Updates commprod recommnedation list for each user'

    def handle(self, **options):
        print "Making CommProdRecs"
        commprods = CommProd.objects.all();

        active_users = UserProfile.objects.filter(user__is_active = True)

        for user_profile in active_users:
            print user_profile.user.username
            for commprod in commprods:
                rec = CommProdRec.objects.get_or_create(user_profile = user_profile, commprod = commprod)
                rec.update_scores()

        print "Complete"

