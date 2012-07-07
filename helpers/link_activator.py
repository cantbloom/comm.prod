""" Given a parge and a request type (trending, popular, recent
etc) returns a tuple of (template_key, template_value, request).
"""
def get_active_page(pageName, requestType):
    template_values = {
    'home' : {
            "" : 'subnav_home',
            "trending" : 'subnav_trending',
            "popular" : 'subnav_popular',
            "recent" : 'subnav_recent',
        },
    'profile' : {
            "" : 'subnav_statistics',
            "statistics" : 'subnav_statistics',
            "popular" : 'subnav_popular',
            "recent" : 'subnav_recent',
        },
    }
    try: 
        result = (template_values[pageName][requestType], "active", requestType)
    except KeyError:
        result = ("", "active", "")
    return result