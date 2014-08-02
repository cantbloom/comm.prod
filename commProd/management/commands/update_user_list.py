#! /usr/bin/env python

from django.core.management.base import NoArgsCommand
import commProd.models as cpm
import os

class Command(NoArgsCommand):
    help = 'Updates autocomplete for the user list.'

    def handle(self, **options):
        print "Updating user list...\n"
        profiles = cpm.UserProfile.objects.all().select_related()
        user_list = []
        user_dict = {}
        for profile in profiles.iterator():
            username = profile.user.username
            name = profile.user.get_full_name()
            if not name:
                name = username
            user_dict[name] = username
            user_list.append(name)
            print "Added", name
        
        data = """
            var user_list = %(user_list)s\n
            var user_dict = %(user_dict)s""" % {
                'user_list' : user_list,
                'user_dict' : user_dict,
            }

        path = os.path.abspath(
            os.path.join('commerical_production/public/js/',
             os.path.pardir))
        path = "%s/js/user_list.js" % path  
        
        with open(path, 'w') as f:
            f.write(data)
        
        print "Complete.\n"

