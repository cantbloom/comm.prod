from django.db import models
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Avg
from datetime import date

 
class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    #other fields here

    activation_key = models.CharField(max_length=40, default='')
    alt_email = models.EmailField(default='')
    send_mail = models.BooleanField(default=False)
    avg_score = models.FloatField(default=0.0)

    def update_avg(self):
        self.avg_score = Rating.objects.filter(commprod__user=self.user).aggregate(Avg('score'))['score__avg']
        self.save()

    """
    Takes an email, updates commprod objects 
    associatd with the alt_email user to self. 
    Also updates Rating objects to self
    """
    def mergeAndDelete(self, email):
        to_delete = User.objects.filter(user__email=email)
        if to_delete.exists():
            CommProd.objects.filter(user=to_delete).update(user=self)
            Rating.objects.filter(user=to_delete).update(user=self)
            to_delete.delete()

    def __str__(self):  
          return "%s's profile" % self.user  

User.profile = property(lambda u: u.get_profile())

class ShirtName(models.Model):
    user = models.ForeignKey(User)

    number = models.CharField(max_length=40, default='')
    name = models.CharField(max_length=40, default='Human Jizz Rag')
    year = models.IntegerField()

class CommProd(models.Model):
	user = models.ForeignKey(User)

	commprod_content = models.TextField() 
	email_content = models.TextField()
	avg_score = models.FloatField(default=0.0)
	date = models.DateTimeField(auto_now=True)

	def update_avg(self):
		self.avg_score = Rating.objects.filter(commprod=self).aggregate(Avg('score'))['score__avg']
		self.save()

	def __unicode__(self):
		return 'a btb "%s" comm.prod by %s on %s' % (self.commprod_content, self.user.username, str(self.date))

class Rating(models.Model):
	commprod = models.ForeignKey(CommProd)
	user = models.ForeignKey(User)

	score = models.FloatField(default=0.0) 
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s voted a %s on commprod_id %s on %s " % (self.user.username, self.score, self.commprod.id, self.date)

#fuck.
import signals
signals.setup()
