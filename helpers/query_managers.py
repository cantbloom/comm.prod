from django.contrib.auth.models import User
from django.db.models import Max, Min

from commProd.models import CommProd, Rating, UserProfile, TrendData
from commprod_search import commprod_search

from helpers.renderers import commprod_renderer, profile_renderer

import random, numpy as np


""" Takes in a get request's dictionary of
values and returns an HTMl template based on the search query
"""
def commprod_query_manager(get_dict, username=None, return_type = "html"):
    valid_params = ['cp_id', 'query', 'direction', 'username', 'startDate', 'endDate', 'limit', 'unvoted']

    valid_types = {
        'popular' : {
                    'orderBy': 'avg_score', 
                    'direction': 'lh',
        },
        'recent' : {
                    'orderBy': 'date', 
                    'direction':'lh',
        },
        'trending' : {
                'orderBy': 'trending_score', 
                'direction':'lh',
        }
    }
    
    search_params = {k : v for k, v in get_dict.items() if k in valid_params}

    ## overwrite given parameters with default for type.
    type = get_dict.get('type', None)
    if type in valid_types:
        search_params = dict(search_params, **valid_types[type])

    if username:
        search_params['username'] = username

    commprods = commprod_search(**search_params)

    return commprod_renderer(commprods, return_type, get_dict.get('page',1))




"""
Handles queries for user data to be displayed on profile page.
"""
def profile_query_manager(user):
    best_score = CommProd.objects.filter(user_profile=user.profile).aggregate(Max('score'))['score__max']
    worst_score = CommProd.objects.filter(user_profile=user.profile).aggregate(Min('score'))['score__min']  

    if best_score == worst_score: 
        query_set = CommProd.objects.filter(user_profile=user.profile, score=best_score)
        best_prod = random.choice(query_set)
        worst_prod = random.choice(query_set)
    
    else: 
        best_prod = CommProd.objects.filter(user_profile=user.profile, score=best_score)[0]
    
        worst_prod = CommProd.objects.filter(user_profile=user.profile, score=worst_score)[0]
    #render html
    best_prod, worst_prod = commprod_renderer([best_prod, worst_prod], 'list')

    most_loved, most_hated = find_faves(user)
    response = {
        'best_prod' : best_prod,
        'worst_prod' : worst_prod,
        'most_loved' : most_loved,
        'most_hated' : most_hated,
    }
    return response

""" 
Returns a dictionary of data needed for graphing
data with the given filter. Returns data_points for
graphing, std, mean, and a grade for the given user.
"""
def vs_data_manager(user, filter_year=None):
    profiles = UserProfile.objects.all()
    if filter_year:
        profiles = profiles.filter(class_year=filter_year)
    score_dict = {}
    for profile in profiles:
        score = profile.score
        if score in score_dict:
            score_dict[score] += 1
        else:
            score_dict[score] = 1
    
    std = np.std(np.array(score_dict.keys()))
    mean = np.mean(np.array(score_dict.keys()))
    grade = get_grade(user.profile.score, std, mean)
    vs_data = {
        'data_points' : score_dict.items(),
        'std' : std,
        'mean' : mean,
        'grade' : grade,
    }

    return vs_data

"""
Calculates trend data and returns response
dictionary for given User object
"""
def trend_data_manager(user):
    trend_query_all = TrendData.objects.filter(date__gt=user.date_joined)
    trend_query_class = trend_query_all.filter(user_profile__class_year=user.profile.class_year)
    trend_query_user = trend_query_class.filter(user_profile=user.profile)
    trend_data = {
        'floor_trend' : get_trend_data(trend_query_all),
        'class_trend' : get_trend_data(trend_query_class),
        'user_trend' : get_trend_data(trend_query_user),
    }
    return trend_data


########### Helpers #############
""" 
Finds the highest and least rated bomber from the 
given user. Returns a rendered list of highest and 
lowest profiles found. 
"""
def find_faves(user):
    ratings = Rating.objects.filter(user_profile=user.profile).select_related()

    user_dict = {}
    for rating in ratings:
        username = rating.commprod.user_profile.user.username
        score = rating.score
        if username in user_dict:
            user_dict[username] += score
        else:
            user_dict[username] = score

    most_loved = UserProfile.objects.order_by('?')[0]
    most_hated = UserProfile.objects.order_by('?')[0]
    min_val = 0
    max_val = 0
    if user_dict != {}:
        most_loved = max(user_dict)
        max_val = user_dict[most_loved]
        most_hated = min(user_dict)
        min_val = user_dict[most_hated]

        # not all equal
        if most_loved != most_hated:
            most_loved = UserProfile.objects.filter(user__username=most_loved)[0]
            most_hated = UserProfile.objects.filter(user__username=most_hated)[0]
    
    return  profile_renderer(dict(zip([most_loved, most_hated], [max_val,min_val])))


""" 
Returns a letter grade for a given score,
std, and mean. 
This is the worst code ever. 
"""
def get_grade(user_score, std, mean):
    a = mean + std
    b = mean
    c = mean - std
    d = c - std
    f = d - std
    if user_score >= a:
        return "A"
    elif user_score < a and user_score >= b:
        return "B"
    elif user_score < b and user_score >= c:
        return "C"
    elif user_score < c and user_score >= d:
        return "D"
    else:
        return "F"

"""
Helper for trend data manager.
Returns a list of data point tuples
"""
def get_trend_data(query_set):
    return [(trend.date, trend.score) for trend in query_set]
