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
    pic_url = models.CharField(max_length=1000, default="/public/img/placeholder.jpg")

    def update_avg(self):
        #self.avg_score = self.user.ratings__set.aggregate(Avg('score'))['score__avg']
        self.avg_score = self.score / CommProd.objects.filter(user_profile=self).count()
        self.save()
    
    def to_json(self):
        return json.dumps({
            'username': self.user.username,
            'name' : self.user.first_name + " " + self.user.last_name,
            })

    """
    Takes an email, updates commprod objects 
    associatd with the alt_email user to self. 
    Also updates Rating objects to self
    """
    def mergeAndDelete(self, email):
        to_delete = User.objects.filter(user__email=email)
        if to_delete.exists():
            to_delete = to_delete[0].profile
            #to_delete.commprod__set.update(user=self)
            #to_delete.rating__set.update(user=self)

            #delete when above is confirmed to work
            CommProd.objects.filter(user_profile=to_delete).update(user_profile=self)
            Rating.objects.filter(user_profile=to_delete).update(user_profile=self)
            
            to_delete.delete()

    def __str__(self):  
          return "%s's profile" % self.user  

User.profile = property(lambda u: u.get_profile())

class ShirtName(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    number = models.CharField(max_length=40, default='')
    name = models.CharField(max_length=40, default='Human Jizz Rag')
    year = models.IntegerField()

class CommProd(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    commprod_content = models.TextField()
    email_content = models.TextField()
    avg_score = models.FloatField(default=0.0)
    date = models.DateTimeField()

    def update_avg(self):
    	self.avg_score = Rating.objects.filter(commprod=self).aggregate(Avg('score'))['score__avg']
    	self.save()    

    def calculate_score(votes, item_hour_age, gravity=1.8):
        return (votes - 1) / pow((item_hour_age+2), gravity)

	def __unicode__(self):
		return 'a btb "%s" comm.prod by %s on %s' % (self.commprod_content, self.user_profile.user.username, str(self.date))

class Rating(models.Model):
    commprod = models.ForeignKey(CommProd)
    user_profile = models.ForeignKey(UserProfile)

    score = models.FloatField(default=0.0)
    previous_score = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, **kwargs):
        super(Rating, self).save(force_insert, force_update)
        diff = self.score - self.previous_score
        self.commprod.update_score(diff)
        self.commprod.user_profile.update_score(diff)

    def __unicode__(self):
    	return "%s voted a %s on commprod_id %s on %s " % (self.user_profile.user.username, self.score, self.commprod.id, self.date)

#fuck.
import signals
signals.setup()
