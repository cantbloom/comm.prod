from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User

from django.conf import settings


class Command(NoArgsCommand):
    help = """Removes 500 error from users 
    that are not registered."""

    def handle(self, **options):
        self.stdout.write('Beginning update...\n')
        users = User.objects.all()
        for user in users:
            if not user.is_active:
                self.stdout.write('Updating %s\n' %
                                  user.username)
                password = User.objects.make_random_password()
                user.set_password(password)
                user.save()

        self.stdout.write('Update complete.\n')
