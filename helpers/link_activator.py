def get_active_page(pageName, requestType):
    """ 
        Given a page and a request type 
        (trending, best, recent, etc) returns 
        a tuple of (template_key, template_value, request).
    """
    template_values = {
        'home': {
            "": 'subnav_home',
            "trending": 'subnav_trending',
            "best": 'subnav_best',
            "worst": 'subnav_worst',
            "recent": 'subnav_recent',
            "media": 'subnav_media'
        },
        'profile': {
            "": 'subnav_statistics',
            "statistics": 'subnav_statistics',
            "best": 'subnav_best',
            "worst": 'subnav_worst',
            "recent": 'subnav_recent',
            "media": 'subnav_media',
            "favorites": 'subnav_favorites'
        },
    }
    try:
        result = (template_values[pageName][requestType],
                  "active", requestType)
    except KeyError:
        # returning '_' avoids index error at view on split('_')
        result = ("_", "active", "")
    return result
