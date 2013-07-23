import commProd.models as cpm
import donations.models as dm

from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.core.validators import \
validate_email as _validate_email
from django.core.exceptions import ValidationError
from django.utils import simplejson as json
from django.db.models import Sum
from annoying.decorators import render_to
from helpers.commprod_search import commprod_search

from datetime import date, datetime, timedelta

import random
import re
import math
import copy

def get_rand_username(user):
    """
        Returns a username to be rendered choosing randomly between
        first + last, username, and a shirt first_name.
    """
    potentials = [shirtname.name 
    for shirtname in cpm.ShirtName.objects.filter(
        user_profile=user.profile)]

    name = user.first_name.strip()
    if not name:
        potentials.append(name)
    else:
        potentials.append(user.username)
    return random.choice(potentials)

@render_to("snippets/hero_err_template.html")
def render_err_msg(request, hero_title, page_title='Oops'):
    """
        Give helpful messages for the retards.
        Returns a hero_err_template with the given data.
        Return this function to give user back an error page.
    """
    prof_href = "/"
    if request.user.is_authenticated:
        prof_href = "user/%s" % request.user.username
    
    return dict(
        page_title=page_title,
        user_profile=prof_href,
        hero_err_title=hero_title,
    )

def possesive(name, title):
    """
        Returns proper ingrish for user profile page
    """
    if unicode(name)[-1] == 's':
        result = "%s'" % name
    else:
        result = "%s's" % name
    if not title:
        title = "Profile"
    return "%(result)s %(title)s" % {
        'result' : result,
        'title': title.capitalize(),
    }


def add_usr_to_query(request_dict, username):
    """
        Adds the specified username to the given dictionary
    """
    d = copy.copy(request_dict)
    d['username'] = username
    return d

def vote_commprod(id, score, user):
    """
        Submit vote for a commprod
    """
    success, commprod = valid_prod(id)
    if not success:
        return success, commprod #False, False

    rating, created = cpm.Rating.objects.get_or_create(
        commprod=commprod, user_profile=user.profile)

    return rating, commprod

def fav_commprod(id, user):
    """
        Submit favorite for a commprod
    """
    success, commprod = valid_prod(id)
    if not success:
        return success, commprod #False, False
    fav, created = cpm.Favorite.objects.get_or_create(
        commprod=commprod, user_profile=user.profile)

    return fav

def valid_prod(id):    
    """
        Helper function to valididate commprod for vote or favoriteing
    """
    commprod = commprod_search(cp_id=id)
    if commprod.count() != 1: #make sure commprod is there
        return False, False
    return True, commprod[0]

def vote_correction(id, score, user):
    """
        Submit vote for a correction
    """
    correction = cpm.Correction.objects.filter(id=id)
    if not correction.exists():
        return False, False

    rating, created = cpm.CorrectionRating.objects.get_or_create(
        correction=correction[0], user_profile=user.profile)
    return rating, correction[0]

def JSONResponse(payload):
    """
        Helper to return HttpResponse with json type
        json.dumps the payload given
    """
    return HttpResponse(json.dumps(payload), 
        mimetype='application/json')

def validate_email(email):
    try:
        _validate_email(email)
        return True
    except ValidationError:
        return False

def get_floor_percentile(profile):
    everyone = float(cpm.UserProfile.objects.all().count())
    worse = float(cpm.UserProfile.objects.filter(
        score__lt=profile.score).count())
    return int(worse / everyone * 100 + .5)

def get_day_trend(profile, num_days=30):
    time_threshold = datetime.now() - timedelta(days=num_days)
    trend_points = cpm.TrendData.objects.filter(
        date__gt=time_threshold, user_profile=profile)
    
    old_score = 0
    if trend_points.exists():
      old_score = trend_points[0].score

    return profile.score - old_score

def _get_donation_stats(donations=None, anon_donations=None):
    """
        Helper to yield dotation stats for home and anon page
    """
    if not donations:
        donations = dm.Donation.objects.all()
    if not anon_donations:
        anon_donations = dm.AnonDonation.objects.all()
    
    tot_donations = donations.count() + anon_donations.count()
    sum_donations = 0
    avg_donation = 0
    if tot_donations != 0:
        donations_sum =  donations.aggregate(Sum('amount'))['amount__sum']
        anon_sum = anon_donations.aggregate(Sum('amount'))['amount__sum']
        if not donations_sum:
            donations_sum = 0
        if not anon_sum:
            anon_sum = 0
        sum_donations = donations_sum + anon_sum
        avg_donation = math.ceil(float(sum_donations)/tot_donations)


    return {
        'tot_donations': tot_donations, 
        'sum_donations' : sum_donations,
        'avg_donation' : int(avg_donation),
    }
