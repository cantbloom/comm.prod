from commProd.models import CommProd, Rating, UserProfile, ShirtName
from django.template import RequestContext
from django.shortcuts import render_to_response
import random

"""
Returns a username to be rendered choosing randomly between
first + last, username, and a shirt first_name.
"""
def getRandomUsername(user):
    potentials = list(ShirtName.objects.filter(user_profile=user.profile))
    potentials.append(user.username)
    first_last = user.first_name.strip() + " " + user.last_name.strip()
    if (first_last != " "):
        potentials.append(first_last)
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