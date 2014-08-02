from django.db import models
from commProd.models import UserProfile

class Donation(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    is_anonymous = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    reason = models.TextField()
    amount = models.IntegerField(default=0.0)

    def __unicode__(self):
        return """Donation of $%(amount)s.00 by 
        %(username)s on %(date)s for %(reason)s""" % {
            'amount' : self.amount,
            'username' :  self.user_profile.username(), 
            'date' : self.date,
            'reason' : self.reason,
        }

class AnonDonation(models.Model):

    is_anonymous = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)
    reason = models.TextField()
    name = models.TextField()
    amount = models.IntegerField(default=0.0)

    def __unicode__(self):
        return """AnonDonation by %(name)s of 
        $%(amount)s.00 on %(date)s for %(reason)s""" % {
            'name' : self.name,
            'amount' :  self.amount, 
            'date' : self.date,
            'reason' :  self.reason,
        }