from django.db import models
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Avg

from helpers.admin import email_templates, utils

from datetime import date, datetime, timedelta
import sha, random


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #other fields here

    activation_key = models.CharField(max_length=40, default='')
    class_year = models.IntegerField(default=1933)
    send_mail = models.BooleanField(default=False)
    avg_score = models.FloatField(default=0.0)
    pic_url = models.CharField(max_length=1000, default="/public/img/placeholder.jpg")
    score = models.IntegerField(default=0)
    data_point_count = models.IntegerField(default=0)

    def update_data_point(self, save=True):
        if self.data_point_count % 3: ##change mod value for less granularity
            data_point = TrendData(user_profile=self, score=self.score, avg_score=self.avg_score)
            data_point.save()
        self.data_point_count += 1

        if save:
            self.save()

    def update_avg(self, save=True):
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

    def add_email(self, email):
        email = Email(user_profile=self, email=email)
        email.sendConfirmEmail();
        email.save()


    """
    Takes an email, updates commprod objects
    associatd with the alt_email user to self.
    Also updates Rating objects to self
    """
    def mergeAndDelete(self, email):
        to_delete = User.objects.filter(email=email)
        if to_delete.exists():
            to_delete = to_delete[0].profile

            self.score += to_delete.score
            self.data_point_count += to_delete.data_point_count

            CommProd.objects.filter(user_profile=to_delete).update(user_profile=self)

            CommProdEmail.objects.filter(user_profile=to_delete).update(user_profile=self) #very important!!
            TrendData.objects.filter(user_profile=to_delete).update(user_profile=self)

            self.update_avg()

            to_delete.user.delete()

    def __unicode__(self):
          return "%s's profile" % self.user

User.profile = property(lambda u: u.get_profile())

class Email(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    email = models.EmailField(default='')
    confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True, default=datetime.now())
    activation_key = models.CharField(max_length=40, default=sha.new(sha.new(str(random.random())).hexdigest()[:5]).hexdigest())

    def sendConfirmEmail(self):
        content = email_templates.alt_email['content'] % (self.user_profile.user.first_name, self.email, 'http://commprod.herokuapp.com/confirm_email/' + self.activation_key + '/')
        subject = email_templates.alt_email['subject']
        emails = [self.email]
        utils.emailUsers(subject, content, emails)

        self.removeExpiredEmails() #perform cleanup of unconfirmed emails

    def confirm(self):
        self.confirmed = True
        self.user_profile.mergeAndDelete(self.email)
        self.save()

    def removeExpiredEmails(self):
        time_threshold = datetime.now() - timedelta(hours=24)
        Email.objects.filter(date_created__lt=time_threshold, confirmed=False).delete()

    def __unicode__(self):
        return "%s, confirmed: %s, owned by %s" % (self.email, self.confirmed, self.user_profile.user.username)

class ShirtName(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    number = models.CharField(max_length=40, default='')
    name = models.CharField(max_length=40, default='Human Jizz Rag')
    year = models.IntegerField(default=1933)
    editable = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s, %s, owned by %s" % (self.name, self.number, self.user_profile.user.username)

class CommProdEmail(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    content = models.TextField()
    date = models.DateTimeField()
    subject = models.TextField()

    def __unicode__(self):
        return 'Email with content %s by %s on %s' % (self.content, self.user_profile.user.username, str(self.date))

class CommProd(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    email_content = models.ForeignKey(CommProdEmail)

    content = models.TextField()
    original_content = models.TextField() #fuck corrections
    avg_score = models.FloatField(default=0.0)
    score = models.IntegerField(default=0)
    trending_score = models.IntegerField(default=0)
    date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now=True)

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
        return 'a btb "%s" comm.prod by %s on %s' % (self.content, self.user_profile.user.username, str(self.date))

class Rating(models.Model):
    commprod = models.ForeignKey(CommProd)
    user_profile = models.ForeignKey(UserProfile)

    score = models.IntegerField(default=0)
    previous_score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, **kwargs):
        super(Rating, self).save(force_insert, force_update)
        diff = int(self.score) - int(self.previous_score)
        self.commprod.update_score(diff)

    def __unicode__(self):
    	return "%s voted a %s on commprod_id %s on %s " % (self.user_profile.user.username, self.score, self.commprod.id, self.date)


class TrendData(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    date = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    avg_score = models.FloatField(default=0.0)

    def __unicode__(self):
        return "%s had a score of %s and avg score of %s on %s" % (self.user_profile.user.username, self.score, self.avg_score, str(self.date))

class Correction(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    commprod = models.ForeignKey(CommProd)

    date = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    content = models.TextField()
    active = models.BooleanField(default=True)
    used = models.BooleanField(default=False)

    def update_score(self, diff):
        self.score = self.score + diff
        self.user_profile.score = self.user_profile.score +diff #update user for points

        if self.score == -1:
            self.active = False

        elif self.score == 1:
            Correction.objects.filter(commprod=self.commprod).update(active=False)
            self.active = False
            self.used = True

            self.commprod.content = self.content

        self.save()


    def __unicode__(self):
        return 'Correction by %s with content %s on %s' % (self.user_profile.user.username, self.content, str(self.date))

class CorrectionRating(models.Model):
    correction = models.ForeignKey(Correction)
    user_profile = models.ForeignKey(UserProfile)

    previous_score = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, **kwargs):
        super(CorrectionRating, self).save(force_insert, force_update)
        diff = int(self.score) - int(self.previous_score)
        self.correction.update_score(diff)

    def __unicode__(self):
        return "%s voted a %s on correction_id %s on %s " % (self.user_profile.user.username, self.score, self.correction.id, self.date)


#fuck.
import signals
signals.setup()
