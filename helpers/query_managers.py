from commprod_search import commprod_search
from django.template import loader, Context
from helpers.pagination import paginator

""" Takes in a get request's dictionary of
values and returns an HTMl template based on the search query
"""
def commprod_queryManager(get_dict, username=None):
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

    #return rendered html
    t = loader.get_template('commprod_timeline.html')
    c = Context({
        'commprods': paginator(get_dict.get('page', 1), commprods)
    })
    return t.render(c)