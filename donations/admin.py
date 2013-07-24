import donations.models as dm
from django.contrib import admin

admin.site.register(dm.Donation)
admin.site.register(dm.AnonDonation)