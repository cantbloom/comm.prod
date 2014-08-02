#! /usr/bin/env python

from django.core.management.base import NoArgsCommand
import commProd.models as cpm

from django.utils import simplejson as json

import random

class Command(NoArgsCommand):
    help = 'Updates commprod recommnedation list for each user'

    def handle(self, **options):
        print "Making CommProdRecs..."
        commprods = cpm.CommProd.objects.all().select_related()
        ratings = cpm.Rating.objects.all().select_related()

        active_users = cpm.UserProfile.objects.filter(
            user__is_active=True).select_related()

        to_add = []
        for user_profile in active_users:
            print user_profile.user.username
            ranked_list = []
            for commprod in commprods:
                score = self.calc_score(
                    user_profile, commprod, ratings)
                ranked_list.append((commprod.id, score))

            #was putting worst first
            ranked_list.sort(key=lambda rating: -rating[1])
            ranked_list = [x[0] for x in ranked_list]

            rec, created = cpm.CommProdRec.objects.get_or_create(
                user_profile=user_profile)
            rec.ranked_list = json.dumps(ranked_list)

            rec.save()

    def calc_score(self, user_profile, commprod, ratings):
        #similarity of when commprod was written to when user was on the floor
        year_diff = user_profile.class_year - commprod.date.year
        if abs(year_diff) <= 5:
            time_period = 1.0
        else:
            time_period = 5.0 / (abs(year_diff) * 3.0)

        #how much does user like the author 
        #of the comm.prod (sum up ratings by user for author)
        like_author = 0
        for rating in ratings:
            if rating.user_profile == user_profile \
            and rating.commprod == commprod:
                like_author += rating.score

        #how popular is this author
        author_popularity = commprod.user_profile.score


        #other dimensions that don't need to be computed
        ## commprod.trending_score
        ### commprod.score

        return time_period * 10.0 + max(like_author / 3.0, 5) \
        + max(author_popularity / 10.0, 5) \
        + max(commprod.trending_score / 100.0, 5) \
        + commprod.score * 1.0 + random.random() * 20.0

