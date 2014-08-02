#! /usr/bin/env python

from django.core.management.base import NoArgsCommand
from django.db.models import F
import commProd.models as cpm


class Command(NoArgsCommand):
    help = """Updates the trending score for all of the 
    commprod objects"""

    def handle(self, **options):
        self.stdout.write('Beginning update...\n')
        cpm.CommProd.objects.filter(
            trending_score__gt=0).update(
            trending_score=F('trending_score') - 1)
        cpm.CommProd.objects.filter(
            trending_score__lt=0).update(
            trending_score=0)

        self.stdout.write('Update complete.\n')
