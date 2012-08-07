from django.template.loader import render_to_string

from helpers.pagination import paginator

from commProd.models import *


""" 
Can render a commprod as html block or list of
html items. User is the user requesting the view.
"""
def commprod_renderer(user, commprods, return_type, type=None, page=None, obj_type="commprod"):
    votes = Rating.objects.filter(user_profile__user=user)
    upvoted = votes.filter(score__gt=0).values_list('commprod__id', flat=True)
    downvoted = votes.filter(score__lt=0).values_list('commprod__id', flat=True)
    favorites = Favorite.objects.filter(user_profile__user=user, fav=True).values_list('commprod__id', flat=True)
    if return_type == "html":
        template_values =  {
            'commprods' : paginator(page, commprods),
            'upvoted' : upvoted,
            'downvoted' : downvoted,
            'favorites' : favorites,
            'obj_type' : obj_type,
        }
        print template_values
        if type:
            template_values['link_mod'] = "&type=" + type

        return render_to_string('commprod/timeline.html',template_values)

    elif return_type == "list":       
        commprod_list = []
        for commprod in commprods:
           upvote_selected, downvote_selected = vote_select(commprod, upvoted, downvoted)
           fav_selected = fav_select(commprod, favorites)
           commprod_list.append(str(render_to_string('commprod/commprod_template.html', 
                {
                    'commprod' : commprod,
                    'upvote_selected' : upvote_selected,
                    'downvote_selected' : downvote_selected,
                    'fav_selected' : fav_selected,
                    'obj_type' : obj_type,
                }))
            )

        return commprod_list

""" 
Input is a dictionary of UserProfile : score.
Renders a user information block as a list of
html items.
"""
def profile_renderer(profiles):
    html_list = []
    for profile in profiles:
        c = {
        'user_profile': profile, 
        }
        html_list.append(render_to_string('profile_template.html', c))
    # happens when only one user profile is found
    if len(html_list) == 1:
        html_list += html_list

    return html_list

""" 
Input is a list of Corrections to render
Renders a correction  block as a list of
html items.
"""
def correction_renderer(user, corrections):
    votes = Correction.objects.filter(correctionrating__user_profile__user=user)
    upvoted = votes.filter(score__gt=0).values_list('id', flat=True)
    downvoted = votes.filter(score__lt=0).values_list('id', flat=True)
    html_list = []
    for correction in corrections:
        upvote_selected, downvote_selected = vote_select(correction, upvoted, downvoted)
        c = {
        'commprod': correction,
        'upvote_selected': upvote_selected ,
        'downvote_selected': downvote_selected,
        'obj_type' :'correction' #correction css class
        }
        html_list.append(render_to_string('commprod/commprod_template.html', c))

    return html_list

def vote_select(obj, upvoted, downvoted):
    upvote_selected = ''
    downvote_selected = ''
    if obj.id in upvoted:
        upvote_selected = 'selected'
    elif obj.id in downvoted:
        downvote_selected = 'selected'
    return upvote_selected, downvote_selected

def fav_select(obj, favorites):
    fav = False
    if obj.id in favorites:
        fav = True
    return fav