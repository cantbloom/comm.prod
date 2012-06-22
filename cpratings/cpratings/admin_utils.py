import os
from django.contrib.auth.models import User

def a(filePath): #add_users_from_file
    #print os.getcwd()
    #print os.path.join(os.getcwd(), filePath)
    f = open(filePath, 'r')
    for email in f:
        email = email.rstrip(os.linesep)
        if '@' not in email:
            email += '@mit.edu'

        username , host = email.split('@')
        user = User.objects.create_user(username=username, email = email, password = User.objects.make_random_password())
        user.save()


