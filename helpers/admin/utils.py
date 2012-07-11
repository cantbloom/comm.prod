from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from email_templates import registration

import os, sha, re, random


"""
ssh to athena and:

blanche bombers > bombers.txt
blanche btb-alum >> bombers.txt

Replace bombers.txt that lives in comm.prod
Use this to add new users the database each year:

python manage.py shell

import helpers.admin.utils as admin
admin.add_users('bombers.txt')
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


"""
Create a new user with the given parameters
"""
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


"""
Email current users 
user_emails is a list of emails to send to.
"""
def emailUsers(subject, html_content, user_emails):
    text_content = strip_tags(html_content)
    from_email = 'kanter@mit.edu'
    msg = EmailMultiAlternatives(subject, text_content, from_email, user_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()



"""
Send an email to inactive users who 
have permission to receive mail to register
"""
def emailInactive():
    users = User.objects.filter(is_staff = True)
    for user in users:
        content = registration['content'] % (user.username, 'http://localhost:8000/register/'+user.profile.activation_key + '/')
        subject = registration['subject']
        emails = [user.email]
        print content, subject, emails
        emailUsers(subject, content, emails)

    return 'done'

"""
Test your regexs
"""
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

