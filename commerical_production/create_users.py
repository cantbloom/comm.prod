from django.contrib.auth.models import User
import os, sha, random

"""
ssh to athena and blanche bombers > bombers.txt

use this to add new users the database each year

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

            username , host = email.split('@')
            
            #user = User.objects.get(username=username)
            init_data = {
                username : username,
                email : email,
                activation_key : sha.new(sha.new(str(random.random())).hexdigest()[:5]+username).hexdigest()
            }
            print init_data
            user = createUser(**init_data)
                                    
        f.close()
    except IOError:
        print "File not found, your current working directory is", os.getcwd()
        print "Tried path:", os.getcwd() + "/" +filePath
        print "What is the actual path?"

def createUser(username, email, activation_key):
    u = User.objects.create_user(username, email)
    u.is_active = False
    u.save()
    user.profile.activation_key = sha.new(sha.new(str(random.random())).hexdigest()[:5]+username).hexdigest()
    user.profile.save()
    return u

def createExtenedUser(init_data):
    pass

add_users('bombers.txt')