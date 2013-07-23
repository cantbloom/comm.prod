#! /usr/bin/env python

from django.core.management.base import NoArgsCommand
import commProd.models as cpm

class Command(NoArgsCommand):
    help = 'Adds a trend data point for all users'
    def handle(self, **options):
        self.stdout.write('Beginning update...\n')
        # should write custom queryset method.
        users = cpm.UserProfile.objects.all() 
        for user in users:
            user.update_data_point()
            self.stdout.write('Added trend data for %s\n' % \
            	user.user.username)

        self.stdout.write('Update complete.\n')