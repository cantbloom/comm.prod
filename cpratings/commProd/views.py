from commProd.models import CommProd, Ratings
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import simplejson

"""
Landing page, top ten rated comm prods + ten newest commprods 
"""
def index(request):

    ##TODO
    template_values = {

    }
    return render_to_response('homepage.html', template_values)

"""
User profile page, 
displays avg. overall score + list of commprods
"""
def user(request):
    ##TODO

    template_values = {

    }
    return render_to_response('commProd/user.html', template_values)


#todo but problbly not dodo
def search(request):
    data  = 'a'
    data = simplejson.dumps(data)

    return HttpResponse(data, mimetype='application/json')
