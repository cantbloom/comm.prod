from django.contrib.auth.models import User
from django.db.models import Max, Min, Sum

from commProd.models import CommProd, Rating, UserProfile, TrendData, Correction
from commprod_search import commprod_search

from helpers.renderers import commprod_renderer, profile_renderer, correction_renderer

from datetime import datetime
import random, time, operator, numpy as np


""" 
Takes in a get request's dictionary of
values and returns an HTMl template based on the search query
"""
def commprod_query_manager(get_dict, user, return_type="html"):
    valid_params = ['cp_id', 'query', 'direction', 'username', 'startDate', 'endDate', 'limit', 'unvoted', 'orderBy']

    valid_types = {
        'best' : {
                    'orderBy': 'score', 
                    'direction': 'lh',
        },
        'worst':{
                'orderBy': 'score', 
                'direction': 'hl',
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

    if 'unvoted' in search_params:
        search_params['unvoted'] = user.username
        
    commprods = commprod_search(**search_params)

    return commprod_renderer(user, commprods, return_type, type, get_dict.get('page',1))




"""
Handles queries for user data to be displayed on profile page.
"""
def profile_query_manager(user, profile_user):

    best_prod, worst_prod = find_profile_prods(user, profile_user)

    most_loved, most_hated = find_profile_faves(profile_user)
    
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
    try:
	first_trend_date = TrendData.objects.filter(user_profile=user.profile).order_by('date')[0].date
    except IndexError:
	first_trend_date = datetime.now()
    trend_query_all = TrendData.objects.filter(date__gt=first_trend_date)
    trend_query_class = trend_query_all.filter(user_profile__class_year=user.profile.class_year)
    trend_query_user = trend_query_class.filter(user_profile=user.profile)
    trend_data = {
        'floor_trend' : get_trend_data(trend_query_all),
        'class_trend' : get_trend_data(trend_query_class),
        'user_trend' : get_trend_data(trend_query_user),
    }
    return trend_data

"""
Finds and renders active corrections for the given commprod
"""
def correction_query_manager(user, correction_id=None, commprod=None):

    corrections = None
    if correction_id:
        corrections =  Correction.objects.filter(id=correction_id, active=True)
    
    elif commprod:
        corrections = Correction.objects.filter(commprod=commprod, active=True)
    
    if corrections and corrections.exists():
        return correction_renderer(user, corrections) 
    else:
        return []


########### Helpers #############
"""
Finds the best and worst commprods for a given profile if they
exist. If none exists boolean is sent back and nothing is
rentered.
"""

def find_profile_prods(user, profile_user):
    if CommProd.objects.filter(user_profile=profile_user.profile).exists():
        best_score = CommProd.objects.filter(user_profile=profile_user.profile).aggregate(Max('score'))['score__max']
        worst_score = CommProd.objects.filter(user_profile=profile_user.profile).aggregate(Min('score'))['score__min']  

        #all prods are the same, just return random
        if best_score == worst_score: 
            query_set = CommProd.objects.filter(user_profile=profile_user.profile, score=best_score)
            best_prod = random.choice(query_set)
            worst_prod = random.choice(query_set)
        
        #otherwise return best/worst prods
        else: 
            best_prod = CommProd.objects.filter(user_profile=profile_user.profile, score=best_score)[0]
        
            worst_prod = CommProd.objects.filter(user_profile=profile_user.profile, score=worst_score)[0]
        
        #render html
        best_prod, worst_prod = commprod_renderer(user, [best_prod, worst_prod], 'list')
    else:
        best_prod = False
        worst_prod = False

    return best_prod, worst_prod

"""
Finds the highest and least rated bomber from the 
given user. Returns a rendered list of highest and 
lowest profiles found. 
"""
def find_profile_faves(profile_user):
    ratings = Rating.objects.filter(user_profile=profile_user.profile).select_related()

    sorted_users = Rating.objects.filter(user_profile=profile_user.profile).values('commprod__user_profile').order_by('commprod__user_profile').annotate(total=Sum('score')).order_by('total')

    try:
        most_hated = UserProfile.objects.get(id=sorted_users[0]['commprod__user_profile'])
        most_loved =  UserProfile.objects.get(id=sorted_users.reverse()[0]['commprod__user_profile'])

    except:
        most_loved = UserProfile.objects.order_by('?')[0]
        most_hated = UserProfile.objects.order_by('?')[0]

    return  profile_renderer([most_loved, most_hated])


""" 
Returns a letter grade for a given score,
std, and mean. 
This is the worst code ever. 
"""
def get_grade(user_score, std, mean):
    letters = ['A', 'B', 'C', 'D', 'F']
    grades = []
    scores = []
    curr_std = 1.33

    if std == 0:
        return 'B'

    #make grades
    for letter in letters:
        grades.append(letter+'+')
        scores.append(mean+std*curr_std)
        curr_std-=.33

        grades.append(letter)
        scores.append(mean+std*curr_std)
        curr_std-=.33

        grades.append(letter+'-')
        scores.append(mean+std*curr_std)
        curr_std-=.33

    scores.append(user_score)
    scores.sort()
    grades.reverse()

    index = max(0, scores.index(user_score)-1)
    return grades[index]


"""
Helper for trend data manager.
Returns a list of data point tuples
"""
def get_trend_data(query_set):
    return [(time.mktime(trend.date.timetuple())*1000, trend.score) for trend in query_set]
