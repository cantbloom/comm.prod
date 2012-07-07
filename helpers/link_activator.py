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
    'profile_trends' : {
        "" : 'vs_class_tab',
        "vs_class" : 'vs_class_tab',
        "vs_floor" : 'vs_floor_tab',
        "trends" : 'trends_tab',
        },
    }
    try: 
        result = (template_values[pageName][requestType], "active", requestType)
    except KeyError:
        result = ("", "active", "")
    return result