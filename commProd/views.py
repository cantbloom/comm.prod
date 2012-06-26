from commProd.models import CommProd, Rating, UserInfo
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.utils import simplejson as json
from cloudmailin.views import MailHandler
from commProd.utils import parseProd    
import re
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

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
    data = json.dumps(data)

    return HttpResponse(data, mimetype='application/json')


def processMail(**kwargs):
    sender = kwargs['x_from_header']
    sender = sender[2:len(sender)-2] #strip crap
    content = kwargs['plain'] 

    email_search = User.objects.filter(email__exact=sender)
    alt_email_search = UserInfo.objects.filter(alt_email__exact=sender)

    if len(email_search) == 1:
        user_id = email_search[0].id
    elif len(alt_email_search) == 1:
        user_id = alt_email_search[0].user_id
    else:
        logger.info("User not found with email address %s" % sender)
        return 
        
    parsed_content = parseProd(content)
    if parsed_content:
        for prod in parsed_content:
            cp = CommProd(content=content, comm_prod=prod, author=user_id)
            cp.save()
            logger.info("Commprod found from email %s with commprod %s" % (sender, prod))
        return 

    logger.info("No commprod found from email %s with content %s" % (sender, content))
    
    return 


mail_handler = MailHandler()

mail_handler.register_address(
    address='00a95f15950afd5d7e13@cloudmailin.net',
    callback=processMail
)

