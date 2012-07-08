from django.template.loader import render_to_string

from helpers.pagination import paginator

from commProd.models import CommProd, Rating, UserProfile, ShirtName


""" 
Can render a commprod as html block or list of
html items. User is the user requesting the view.
"""
def commprod_renderer(user, commprods, return_type, type=None, page=None):
    votes = CommProd.objects.filter(rating__user_profile__user = user)
    upvoted = votes.filter(score__gt = 0).values_list('id', flat=True)
    downvoted = votes.filter(score__lt = 0).values_list('id', flat=True)
    print return_type
    if return_type == "html":
        template_values =  {
            'commprods': paginator(page, commprods),
            'upvoted': upvoted,
            'downvoted': downvoted
        }
        if type:
            template_values['link_mod'] = "&type=" + type

        return render_to_string('commprod_timeline.html',template_values)

    elif return_type == "list":       
        commprod_list = []
        for commprod in commprods:
            if commprod.id in upvoted:
                upvote_selected = 'selected'
                downvote_selected = ''
            elif commprod.id in downvoted:
                upvote_selected = ''
                downvote_selected = 'selected'
            else:
                upvote_selected = ''
                downvote_selected = ''
            
            commprod_list.append(
                str(render_to_string('commprod.html', {
                    'commprod': commprod,
                    'upvoted_selected': upvote_selected ,
                    'downnvoted_selected': downvote_selected
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
        'score' : profiles[profile],
        }
        html_list.append(render_to_string('profile_template.html', c))

    return html_list