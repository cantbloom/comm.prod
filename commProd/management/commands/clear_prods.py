from django.core.management.base import NoArgsCommand
from commProd.models import CommProd, Rating, UserProfile, CommProdEmail, TrendData


class Command(NoArgsCommand):
    help = 'Deletes all of the commprod, rating and trendata points. Updates all of the UserProfile objects to have a score and avg score of zero.'
    def handle(self, **options):
        self.stdout.write('CAUTION! This will reset the database dumping all commprods, ratings, and trendata and also delete user scores. \n')
        ans = raw_input('Continue?(y/n) ')
        if ans.lower() in ['y', 'yes']:
            ans = raw_input("You sure you sure? ")
            if ans.lower() == "very sure":
                self.clear_db()


    def clear_db(self):
        self.stdout.write('Deleting commprods...\n')
        #deletes all correction objects which deletes all correction ratings
        CommProd.objects.all().delete()
        self.stdout.write('Deleting commprod emails...\n')
        CommProdEmail.objects.all.delete()
        self.stdout.write('Deleting ratings...\n')
        Rating.objects.all().delete()
        self.stdout.write('Deleting TrendData...\n')
        TrendData.objects.all().delete()
        self.stdout.write('Updating UserProfile...\n')
        UserProfile.objects.all().update(score=0, avg_score=0)
        self.stdout.write('Update complete.\n')