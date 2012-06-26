import os
import re
from django.contrib.auth.models import User
from django.db import IntegrityError


"""
ssh to athena and blanche bombers > bombers.txt

use this to add new users the database each year

python manage.py shell

>>> import commerical_production.admin_utils as utils
>>> utils.add_users('bombers.txt')
"""

def add_users(filePath):

    try:
        f = open(filePath)

        for email in f:
            email = email.rstrip(os.linesep)
            if '@' not in email:
                email += '@mit.edu'

            username , host = email.split('@')
            try:
                user, created = User.objects.get_or_create(username=username, email=email, password=User.objects.make_random_password())
                user.save()
                print email + " | " + str(created)
            except IntegrityError:
                print email + " | " + str(False)
                continue
        
        f.close()
    except IOError:
        print "File not found, your current working directory is", os.getcwd()
        print "Tried path:", os.getcwd() + "/" +filePath
        print "What is the actual path?"

def testRegex():
    while True:
        cmd = raw_input("Type EXIT to quit, press enter to continue: ")
        if cmd == "EXIT":
            break
        pattern =  re.compile(raw_input("Enter your regex: "))
        query = raw_input("Enter input string to search: ")
        if pattern.search(query) == None:
            print "No match found"
        
        else:

            for m in pattern.finditer(query):
                print "\nI found the text '%s' starting at index '%d' and ending at index '%d'." % (m.group(), m.start(), m.end())