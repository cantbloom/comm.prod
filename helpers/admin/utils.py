from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings

from email_templates import registration, sorry_email

import os, sha, re, random

def add_users(filePath):

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
    """
    Create a new user with the given parameters
    """
    try:
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.is_active = False
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            if send_mail:
                user.profile.activation_key = sha.new(sha.new(str(random.random())).hexdigest()[:5]+username).hexdigest()
                user.profile.send_mail = send_mail
                user.profile.save()
        return user, created
    except IntegrityError:
        return None


def emailUsers(subject, html_content, user_emails, from_email='bombers@mit.edu'):
    """
    Email current users
    user_emails is a list of emails to send to.
    """
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, user_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def emailInactive(alums=False):
    """
    Send an email to inactive users who
    have permission to receive mail to register
    """
    users = User.objects.filter(is_active=False, userprofile__send_mail=True)
    if not alums:
        users = users.filter(email__contains='@mit.edu')
    for user in users:
        sendRegEmail(user.username)

    return 'done'

def emailSendMailFalse(alums=False):
    """
    Send an email to can't send
    """
    users = User.objects.filter(userprofile__send_mail=False)
    for user in users:
      print user
      sendSorryEmail(user.username)

    return 'done'

def testRegex():
    """
    Test your regexs
    """
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

def sendRegEmail(username):
    """
    Send reg email to given user
    """
    user = User.objects.get(username = username)
    if user:
        content = registration['content'] % (user.username, settings.BASE_URL_PROD + '/register/' + user.profile.activation_key + '/')
        subject = registration['subject']
        emails = [user.email]
        emailUsers(subject, content, emails)
        return True
    else:
        return False

def sendSorryEmail(username):
    """
    Send sorry email to given user
    """
    user = User.objects.get(username=username)
    if user:
        content = sorry_email['content'] % (user.username)
        subject = sorry_email['subject']
        emails = [user.email]
        emailUsers(subject, content, emails)
        return True
    else:
        return False