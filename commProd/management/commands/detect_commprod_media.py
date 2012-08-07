from django.core.management.base import NoArgsCommand
from commProd.models import *
from helpers.view_helpers import commprod_contains_media


class Command(NoArgsCommand):
    help = "Detects if a commprod contains media (url, img, youtube video) and updates the column appropiately."
    def handle(self, **options):
        self.stdout.write("Starting...\n")
        commprods = CommProd.objects.all()
        for commprod in commprods:
            media = commprod_contains_media(commprod.content)
            self.stdout.write("Updating commprod id %s, media? %s\n" % (commprod.id, media))
            commprod.media = media
            commprod.save()
        self.stdout.write("Done.\n")