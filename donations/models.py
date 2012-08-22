from django.db import models
from commProd.models import UserProfile

class Donation(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    is_anonymous = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField(default=0.0)
    reason = models.TextField()
