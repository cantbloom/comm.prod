from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required
from commProd.models import CommProd, Rating, UserInfo
from cloudmailin.views import MailHandler
import re

"""
Landing page, top ten rated comm prods + ten newest commprods 
"""
@login_required
def home(request):

    ##TODO
    template_values = {

    }
    return render_to_response('home.html', template_values)

"""
User profile page, 
displays avg. overall score + list of commprods
"""
@login_required
def user(request):
    ##TODO

    template_values = {

    }
    return render_to_response('commProd/user.html', template_values)

@login_required
def search(request):
    data  = 'a'
    data = json.dumps(data)

    return HttpResponse(data, mimetype='application/json')


def processMail(request):
    data = request.POST["data"]
    resp = ""
    if data:
        data = json.loads(data) #[{sender : (content, comm_prods)}]
        for dic in data:
            sender = dic.keys()[0]
            content = dic[sender][0]
            comm_prods = dic[sender][1]

            email_search = User.objects.filter(email__exact=sender)
            alt_email_search = UserInfo.objects.filter(alt_email__exact=sender)

            if len(email_search) == 1:
                user_id = email_search[0].id
            elif len(alt_email_search) == 1:
                user_id = alt_email_search[0].user_id
            else:
                resp += "User %s not found\n" % sender
            
            for prod in comm_prods:
                cp = CommProd(content=content, comm_prod=prod, author=user_id)
                cp.save() 
    else:
        resp = "No data"
    return HttpResponse(resp, mimetype="text/plain")


