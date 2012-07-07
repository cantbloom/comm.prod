from django.template import loader, Context

from helpers.pagination import paginator

""" 
Can render a commprod as html block or list of
html items.
"""
def commprod_renderer(commprods, return_type, page=None):
    if return_type == "html":
        t = loader.get_template('commprod_timeline.html')
        c = Context({
            'commprods': paginator(page, commprods)
        })
        return t.render(c)

    elif return_type == "list":
        t = loader.get_template('commprod.html')
        
        commprod_list = []
        for commprod in commprods:
            c = Context({'commprod': commprod})
            commprod_list.append(t.render(c))

        return commprod_list

""" 
Input is a dictionary of UserProfile : score.
Renders a user information block as a list of
html items.
"""
def profile_renderer(profiles):
    t = loader.get_template('user.html')
    
    html_list = []
    for profile in profiles:
        c = Context({
            'user_profile': profile,
            'score' : profiles[profile],
            })
        html_list.append(t.render(c))

    return html_list