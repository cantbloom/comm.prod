""" Given a parge and a request type (trending, best, recent
etc) returns a tuple of (template_key, template_value, request).
"""
def get_active_page(pageName, requestType):
    template_values = {
    'home' : {
            "" : 'subnav_home',
            "trending" : 'subnav_trending',
            "best" : 'subnav_best',
            "worst" : 'subnav_worst',
            "recent" : 'subnav_recent',
        },
    'profile' : {
            "" : 'subnav_statistics',
            "statistics" : 'subnav_statistics',
            "best" : 'subnav_best',
            "worst" : 'subnav_worst',
            "recent" : 'subnav_recent',
        },
    }
    try: 
        result = (template_values[pageName][requestType], "active", requestType)
    except KeyError:
        result = ("_", "active", "") # returning '_' avoids index error at view on split('_')
    return result
