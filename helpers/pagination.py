from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
Provides pagination for a given list of objects.
Call function for any page needing pagination.
"""

def paginator(request, object_list, per_page=10):

    paginator = Paginator(object_list, per_page) # Show default 10 objects per page

    page = request.GET.get('page')
    
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    return objects