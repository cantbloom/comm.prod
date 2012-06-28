from django.db import models
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class CommProd(models.Model):
	comm_prod = models.TextField() 
	content = models.TextField()
	author = models.IntegerField() # user id of author
	score = models.FloatField(default=0.0)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return 'a btb "%s" comm.prod by %s on %s' % (self.comm_prod, self.author, self.date)

class Rating(models.Model):
	cp_id = models.IntegerField() # comm prod id
	user_id = models.IntegerField()
	vote = models.FloatField() 
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "cp_id %s, user_id %s, vote %s" % (self.cp_id, self.user_id, self.vote)

class UserInfo(models.Model):
	user_id = models.IntegerField()
	alt_email = models.EmailField()
	shirt_names = models.TextField(default=json.dumps(['Human Jizz Rag']))

	def __unicode__(self):
		return "cp_id %s, user_id %s, vote %s" % (self.cp_id, self.user_id, self.vote)
 
class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here

    activation_key = models.CharField(max_length=40, default='')
    alt_email = models.EmailField(default='')
    shirt_names = models.TextField(default=json.dumps(['Human Jizz Rag']))

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

User.profile = property(lambda u: u.get_profile() )