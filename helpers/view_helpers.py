from commProd.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils import simplejson as json

from helpers.commprod_search import commprod_search
from common.constants import REGEX

from datetime import date, datetime, timedelta
import random


"""
Returns a username to be rendered choosing randomly between
first + last, username, and a shirt first_name.
"""
def getRandomUsername(user):
    potentials = [shirtname.name for shirtname in ShirtName.objects.filter(user_profile=user.profile)]

    name = user.first_name.strip()
    if (name != ""):
        potentials.append(name)
    else:
        potentials.append(user.username)
    return random.choice(potentials)

"""
Give helpful messages for the retards.
Returns a hero_err_template with the given data.
Return this function to give user back an error page.
"""
def renderErrorMessage(request, hero_title, page_title='Oops'):
    if request.user.is_authenticated:
        prof_href = "user/" + request.user.username
    else:
        prof_href = "/"
    template_values = {
        'page_title': page_title,
        'user_profile' : prof_href,
        'hero_err_title' : hero_title,
    }
    return render_to_response('hero_err_template.html',
        template_values, context_instance=RequestContext(request))
"""
Returns proper ingrish for user profile page
"""
def possesive(name, title):
    if unicode(name)[-1] == 's':
        result = "%s' " % name
    else:
        result = "%s's " % name
    if title == "":
        title = " Profile"
    return result + title.capitalize()

"""
Adds the specified username to the given dictionary
"""

def addUserToQuery(request_dict, username):
    d = {}
    for key, value in request_dict.items():
        d[key] = value
    d['username'] = username
    return d

"""
Submit vote for a commprod
"""
def vote_commprod(id, score, user):
    success, commprod = valid_prod(id)
    if not success:
        return success, commprod #False, False

    rating, created = Rating.objects.get_or_create(commprod=commprod, user_profile=user.profile)

    return rating, commprod

"""
Submit favorite for a commprod
"""
def fav_commprod(id, user):
    success, commprod = valid_prod(id)
    if not success:
        return success, commprod #False, False
    fav, created = Favorite.objects.get_or_create(commprod=commprod, user_profile=user.profile)

    return fav

"""
Helper function to valididate commprod for vote or favoriteing
"""
def valid_prod(id):    
    commprod = commprod_search(cp_id=id)
    if commprod.count() != 1: #make sure commprod is there
        return False, False
    return True, commprod[0]

"""
Submit vote for a correction
"""
def vote_correction(id, score, user):
    correction = Correction.objects.filter(id=id)
    if not correction.exists():
        return False, False

    rating, created = CorrectionRating.objects.get_or_create(correction=correction[0], user_profile=user.profile)
    return rating, correction[0]

"""
Helper to return HttpResponse with json type
json.dumps the payload given
"""
def JSONResponse(payload):
    return HttpResponse(json.dumps(payload), mimetype='application/json')


"""
Detect if a commprod has media content
"""
def commprod_contains_media(commprod):
    url_regex = REGEX['url_regex']
    pattern = re.compile(url_regex, re.I)
    match = pattern.search(commprod)
    return bool(match)
def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def get_floor_percentile(profile):
    everyone = float(UserProfile.objects.all().count())
    worse = float(UserProfile.objects.filter(score__lt = profile.score).count())
    return int(worse/everyone*100 + .5)

def get_day_trend(profile, num_days=30):
    time_threshold = datetime.now() - timedelta(days=num_days)
    trend_points = TrendData.objects.filter(date__gt=time_threshold, user_profile=profile)
    if trend_points.exists():
      old_score = trend_points[0].score
    else:
      old_score = 0
    return profile.score - old_score
