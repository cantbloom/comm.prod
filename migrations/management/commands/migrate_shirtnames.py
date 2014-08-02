# this won't do everything, you have to fill in stuff. it is just boiler
# plate code
from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
import commProd.models as cpm


class Command(NoArgsCommand):
    help = "Used to migrate old shirtname objects and ratings"

    def handle(self, **options):
        shirtnames = ShirtName.objects.all()

        for shirtname in shirtnames:
            self.stdout.write("shirt id: %s" % shirtname.id)
            shirtname.user_profile = cpm.UserProfile.objects.get(
                user=shirtname.user)
            shirtname.save()

        ratings = Rating.objects.all()
        for rating in ratings:
            self.stdout.write("rating id: %s " % rating.id)
            rating.user_profile = cpm.UserProfile.objects.get(
                user=rating.user)
            rating.save()

        # commprods = cpm.CommProd.objects.all()

        # for commprod in commprods:
        #   print commprod.id
        #   commprod.user_profile = cpm.UserProfile.objects.get(
        #    user=commprod.user)
        #   commprod.save()
