from django.contrib.auth.models import User
from django.db import IntegrityError
import os, sha, random

"""
ssh to athena and:

blanche bombers > bombers.txt
blanche btb-alum >> bombers.txt

Replace bombers.txt that lives in comm.prod
Use this to add new users the database each year:

python manage.py shell

import commerical_production.create_users as create_users
create_users.add_users('bombers.txt')
"""
def add_users(filePath):
    try:
        f = open(filePath)

        for email in f:
            email = email.rstrip(os.linesep)
            if '@' not in email:
                email += '@mit.edu'

            username, host = email.split('@')
            
            init_data = {
                'username' : username,
                'email' : email,
                'send_mail' : True,
            }
            print init_data
            print createUser(**init_data)
                                    
        f.close()
    except IOError:
        print "File not found, your current working directory is", os.getcwd()
        print "Tried path:", os.getcwd() + "/" +filePath
        print "What is the actual path?"

def createUser(username, email, send_mail=False):
    try:
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.is_active = False
            user.save()
            if send_mail:
                user.profile.activation_key = sha.new(sha.new(str(random.random())).hexdigest()[:5]+username).hexdigest()
                user.profile.send_mail = send_mail
                user.profile.save()
        return user, created
    except IntegrityError:
        return None
