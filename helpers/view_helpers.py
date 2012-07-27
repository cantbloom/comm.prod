from commProd.models import CommProd, Rating, UserProfile, ShirtName, Correction, CorrectionRating
from django.template import RequestContext
from django.shortcuts import render_to_response

from helpers.commprod_search import commprod_search

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
def renderErrorMessage(request, page_title, hero_title):
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
    commprod = commprod_search(cp_id=id)
    if commprod.count() != 1:
        return False, False
    commprod = commprod[0]
    rating, created = Rating.objects.get_or_create(commprod=commprod, user_profile=user.profile)

    return rating, commprod

"""
Submit vote for a correction 
"""
def vote_correction(id, score, user):
    correction = Correction.objects.filter(id=id)
    if not correction.exists():
        return None

    rating, created = CorrectionRating.objects.get_or_create(correction=correction[0], user_profile=user.profile)
    return rating, correction[0]

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False
