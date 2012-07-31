#! /usr/bin/env python

from django.core.management.base import NoArgsCommand
from commProd.models import UserProfile


class Command(NoArgsCommand):
    help = 'Adds a trend data point for all users'
    def handle(self, **options):
        self.stdout.write('Beginning update...\n')
        users = UserProfile.objects.all() # should write custom queryset method.
        for user in users:
            user.update_data_point()
            self.stdout.write('Added trend data for %s\n'%user.user.username)

        self.stdout.write('Update complete.\n')