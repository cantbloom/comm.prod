from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginator(page, object_list, per_page=33):
    """
    Provides pagination for a given list of objects.
    Call function for any page needing pagination.
    """
    paginator = Paginator(object_list, per_page) # Show default 10 objects per page
    
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    return objects