from django.template import loader, Context

from helpers.pagination import paginator

from commProd.models import CommProd, Rating, UserProfile, ShirtName


""" 
Can render a commprod as html block or list of
html items.
"""
def commprod_renderer(user, commprods, return_type, page=None):
    votes = CommProd.objects.filter(rating__user_profile__user = user)
    upvoted = votes.filter(score__gt = 0).values_list('id', flat=True)
    downvoted = votes.filter(score__lt = 0).values_list('id', flat=True)

    if return_type == "html":
        print upvoted
        t = loader.get_template('commprod_timeline.html')
        c = Context({
            'commprods': paginator(page, commprods),
            'upvoted': upvoted,
            'downvoted': downvoted
        })
        return t.render(c)

    elif return_type == "list":
        t = loader.get_template('commprod.html')
        
        commprod_list = []
        for commprod in commprods:
            if commprod.id in upvoted:
                upvote_selected = 'selected'
                downvote_selected = ''
            elif commprod.id in downvoted:
                upvote_selected = ''
                downvote_selected = 'selected'

            c = Context({
                'commprod': commprod,
                'upvoted': upvote_selected ,
                'downnvoted': downvote_selected
            })

            commprod_list.append(t.render(c))

        return commprod_list

""" 
Input is a dictionary of UserProfile : score.
Renders a user information block as a list of
html items.
"""
def profile_renderer(profiles):
    t = loader.get_template('profile_template.html')
    
    html_list = []
    for profile in profiles:
        c = Context({
            'user_profile': profile,
            'score' : profiles[profile],
            })
        html_list.append(t.render(c))

    return html_list