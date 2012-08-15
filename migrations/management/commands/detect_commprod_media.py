from django.core.management.base import NoArgsCommand
from helpers.urlize_tags import urlize_commprod, commprod_contains_media
from commProd.models import *

class Command(NoArgsCommand):
    help = "Detects if a commprod contains media (url, img, youtube video) and updates the column appropiately."
    def handle(self, **options):
        self.stdout.write("Starting...\n")
        commprods = CommProd.objects.all()
        for commprod in commprods.iterator():
            media = commprod_contains_media(commprod.content)
            self.stdout.write("Updating commprod id %s, media? %s\n" % (commprod.id, media))
            commprod.media = media
            if media: #write the media content
                commprod.media_content = urlize_commprod(commprod.content)
                print urlize_commprod(commprod.content)
            commprod.save()
        self.stdout.write("Done.\n")