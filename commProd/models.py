from django.db import models
from django.utils import simplejson as json
# Create your models here.

class CommProd(models.Model):
	comm_prod = models.TextField() 
	content = models.TextField()
	author = models.IntegerField() # user id of author
	score = models.FloatField(default=0.0)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return 'a btb "%s"comm.prod by %s on %s' % (self.content, self.author, self.date)

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
