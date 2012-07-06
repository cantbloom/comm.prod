from django.contrib.auth.models import User
from django.db.models import Max, Min

from commProd.models import CommProd, Rating, UserProfile
from commprod_search import commprod_search
from django.template import loader, Context
from helpers.pagination import paginator


""" Takes in a get request's dictionary of
values and returns an HTMl template based on the search query
"""
def commprod_query_manager(get_dict, username=None, returnType="html" ):
    valid_params = ['cp_id', 'query', 'direction', 'username', 'startDate', 'endDate']
    valid_types = {
        'popular' : {
                    'orderBy': 'avg_score', 
                    'direction': 'lh',
        },
        'recent' : {
                    'orderBy': 'date', 
                    'direction':'lh',
        },
    }
    
    search_params = {k : v for k, v in get_dict.items() if k in valid_params}

    ## overwrite given parameters with default for type.
    type = get_dict.get('type', None)
    if type in valid_types:
        search_params = dict(search_params, **valid_types[type])

    if username:
        search_params['username'] = username

    commprods = commprod_search(**search_params)

    return commprod_renderer(commprods, returnType, get_dict.get('page',1))

def commprod_renderer(commprods, returnType, page=None):
    if returnType == "html":
        t = loader.get_template('commprod_timeline.html')
        c = Context({
            'commprods': paginator(page, commprods)
        })
        return t.render(c)
    elif returnType == "list":
        t = loader.get_template('commprod.html')
        
        commprod_list = []
        for commprod in commprods:
            c = Context({'commprod': commprod})
            commprod_list.append(t.render(c))

        return commprod_list

"""
Handles queries for user data to be displayed on profile page.
"""
def profile_query_manager(user):
    best_score = CommProd.objects.filter(user_profile=user.profile).aggregate(Max('score'))['score__max']
    worst_score = CommProd.objects.filter(user_profile=user.profile).aggregate(Min('score'))['score__min']
    best_prod = CommProd.objects.filter(user_profile=user.profile, score=best_score)[0]
    worst_prod = CommProd.objects.filter(user_profile=user.profile, score=worst_score)[0]

    best_prod, worst_prod = commprod_renderer([best_prod, worst_prod], 'list')

    most_loved, max, most_hated, min = find_faves(user)
    response = {
        'best_prod' : best_prod,
        'worst_prod' : worst_prod,
        'most_loved' : (most_loved, max),
        'most_hated' : (most_hated, min),
    }
    return response

def find_faves(user):
    ratings = Rating.objects.filter(user_profile=user.profile)

    user_dict = {}
    max = 0
    min = 0
    most_loved = None
    most_hated = None
    for rating in ratings:
        username = rating.commprod.user_profile.user.username
        score = rating.score
        if username in user_dict:
            user_dict[username] += score
        else:
            user_dict[username] = score
        if user_dict[username] > max:
            max = score
            most_loved = username
        if user_dict[username] < min:
            min = score
            most_hated = username

    if most_loved:
        most_loved = UserProfile.objects.filter(user__username=most_loved)[0]
    else:
        most_loved = UserProfile.objects.order_by('?')[0]
   
    if most_hated:
        most_hated = UserProfile.objects.filter(user__username=most_hated)[0]
    else:
        most_hated = UserProfile.objects.order_by('?')[0]
    
    return  (most_loved, max, most_hated, min)
