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
    class_year = models.IntegerField(default=1933)
    send_mail = models.BooleanField(default=False)
    avg_score = models.FloatField(default=0.0)
    pic_url = models.CharField(max_length=1000, default="/public/img/placeholder.jpg")

    score = models.FloatField(default=0.0)
    data_point_count = models.IntegerField(default=0)

    def update_data_point(self, save=True):
        if self.data_point_count % 3:
            data_point = TrendData(user_profile=self, score=self.score, avg_score=self.avg_score)
            data_point.save()

        self.data_point_count += 1

        if save:
            self.save()

    def update_avg(self, save=True):
        #self.avg_score = self.user.ratings__set.aggregate(Avg('score'))['score__avg']
        self.avg_score = self.score / CommProd.objects.filter(user_profile=self).count()
        if save:
            self.save()

    def update_score(self, diff, save=True):
        self.score = self.score + diff
        self.update_avg(save=False)
        self.update_data_point(save=False)
        if save:
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

    def __unicode__(self):  
          return "%s's profile" % self.user  

User.profile = property(lambda u: u.get_profile())

class ShirtName(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    number = models.CharField(max_length=40, default='')
    name = models.CharField(max_length=40, default='Human Jizz Rag')
    year = models.IntegerField()

    def __unicode__(self):
        return "%s, %s, owned by %s" % name, number, user_profile.user.username

class CommProd(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    commprod_content = models.TextField()
    email_content = models.TextField()
    avg_score = models.FloatField(default=0.0)
    score = models.FloatField(default=0.0)
    trending_score = models.IntegerField(default=0)
    date = models.DateTimeField()

    def update_avg(self, save=True):
    	self.avg_score = Rating.objects.filter(commprod=self).aggregate(Avg('score'))['score__avg']
    	if save:
            self.save()  

    def update_score(self, diff):
        self.score += diff
        self.user_profile.update_score(diff)

        self.update_avg(save=False)

        #there was no previous vote, so register activity
        if abs(diff) == 1:
            self.register_activity(save=False)

        self.save()   

    def register_activity(self, save=True):
        #fiddle with 400 to adjust how long a vote has an effect
        self.trending_score += 400;

        if save:
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
        diff = float(self.score) - float(self.previous_score)
        self.commprod.update_score(diff)

    def __unicode__(self):
    	return "%s voted a %s on commprod_id %s on %s " % (self.user_profile.user.username, self.score, self.commprod.id, self.date)


class TrendData(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    date = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    avg_score = models.FloatField(default=0.0)

    def __unicode__(self):
        return "%s had a score of %s and avg score of %s on %s" % self.user_profile.user.username, self.score, self.avg_score, str(self.datetime)


#fuck.
import signals
signals.setup()
