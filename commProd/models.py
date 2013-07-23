from django.db import models
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.db.models import Avg
from django.conf import settings
from django.utils import timezone
from django.core import management

from helpers.admin import email_templates, utils
from helpers.urlize_tags import urlize_text, \
 commprod_contains_media

from datetime import date, datetime, timedelta
from threading import Lock

from helpers.admin.utils import get_digest

import random

commprod_lock = Lock()
correction_lock = Lock()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #other fields here

    activation_key = models.CharField(max_length=40, 
        default='')
    class_year = models.IntegerField(default=1933)
    send_mail = models.BooleanField(default=False)
    avg_score = models.FloatField(default=0.0)
    pic_url = models.CharField(max_length=1000, 
        default="/public/img/placeholder.jpg")
    score = models.IntegerField(default=0)
    data_point_count = models.IntegerField(default=0)
    use_tour = models.BooleanField(default=True)
    stripe_customer_id = models.CharField(max_length=1000, 
        default="no_id")

    def update_data_point(self, save=True):
        if not self.data_point_count % 1:
            data_point = TrendData(user_profile=self,
             score=self.score, avg_score=self.avg_score)
            data_point.save()
        self.data_point_count += 1

        if save:
            self.save()

    def update_avg(self, save=True):
        self.avg_score = self.score / CommProd.objects.filter(
            user_profile=self).count()
        if save:
            self.save()

    def update_score(self, diff, save=True):
        self.score = self.score + diff
        self.update_avg(save=False)

        if save:
            self.save()

    def to_json(self):
        return json.dumps({
            'username': self.user.username,
            'name' : self.user.get_full_name(),
            })

    def add_email(self, email):
        email = Email(user_profile=self, email=email)
        email.send_confirm_email();
        email.save()

    def merge_and_delete(self, email):   
        """
            Takes an email, updates commprod objects
            associatd with the alt_email user to self.
            Also updates Rating objects to self
        """
        to_delete = User.objects.filter(email=email)
        if to_delete.exists():
            to_delete = to_delete[0].profile

            self.score += to_delete.score
            self.data_point_count += to_delete.data_point_count

            CommProd.objects.filter(
                user_profile=to_delete).update(
                user_profile=self)

            CommProdEmail.objects.filter(
                user_profile=to_delete).update(
                user_profile=self) #very important!!
            TrendData.objects.filter(
                user_profile=to_delete).update(
                user_profile=self)

            self.update_avg()

            management.call_command('update_user_list')
            to_delete.user.delete()

    def username(self):
        return self.user.username

    def __unicode__(self):
          return "%s's profile" % self.user

User.profile = property(lambda u: u.get_profile())

class Email(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    email = models.EmailField(default='')
    confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True, 
        default=datetime.now())
    activation_key = models.CharField(max_length=40, 
        default=get_digest())

    def send_confirm_email(self):
        content = email_templates.alt_email['content'] % \
        (self.user_profile.user.first_name, 
            self.email, '%s/confirm_email/%s/' % \
            (settings.BASE_URL_PROD, self.activation_key))
        subject = email_templates.alt_email['subject']
        emails = [self.email]
        utils.email_users(subject, content, emails)

        self.rm_expired_emails() #perform cleanup of unconfirmed emails

    def confirm(self):
        self.confirmed = True
        self.user_profile.merge_and_delete(self.email)
        self.save()

    def rm_expired_emails(self):
        time_threshold = datetime.now() - timedelta(hours=24)
        Email.objects.filter(date_created__lt=time_threshold, confirmed=False).delete()

    def __unicode__(self):
        return "%(email)s, confirmed: %s, owned by %s" % {
            'email' : self.email,
            'confirmed' : self.confirmed, 
            'username' : self.user_profile.username(),
        }

class ShirtName(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    number = models.CharField(max_length=40, default='')
    name = models.CharField(max_length=40, 
        default='Human Jizz Rag')
    year = models.IntegerField(default=1933)
    editable = models.BooleanField(default=True)

    def __unicode__(self):
        return "%(name)s, %(number)s, owned by %(username)s" % {
            'name' : self.name,
            'number' : self.number,
            'username' : self.user_profile.username(),
        }

class CommProdEmail(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    content = models.TextField()
    date = models.DateTimeField()
    subject = models.TextField()

    def __unicode__(self):
        return """Email with content %(content)s 
        by %(username)s on %(date)s""" % {
            'content' : self.content, 
            'username' : self.user_profile.username(), 
            'date' : self.date,
        }

class CommProd(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    email_content = models.ForeignKey(CommProdEmail)

    content = models.TextField()
    original_content = models.TextField() #fuck corrections
    #commprod with url tags inserted
    media_content = models.TextField()
    avg_score = models.FloatField(default=0.0)
    score = models.IntegerField(default=0)
    trending_score = models.IntegerField(default=0)
    media = models.BooleanField(default=False)
    date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now=True)

    def update_avg(self, save=True):
    	self.avg_score = Rating.objects.filter(
            commprod=self).aggregate(
            Avg('score'))['score__avg']
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
        #fiddle with 400 to adjust how long a 
        #vote has an effect
        self.trending_score += 400;

        if save:
            self.save()

    def calculate_score(votes, item_hour_age, gravity=1.8):
        return (votes - 1) / pow((item_hour_age + 2), gravity)

    def __unicode__(self):
        return """a btb '%(content)s' comm.prod by %(date)s 
        on %(date)s""" % {
            'content' : self.content, 
            'username' : self.user_profile.username(), 
            'date' : self.date
        }

class Rating(models.Model):
    commprod = models.ForeignKey(CommProd)
    user_profile = models.ForeignKey(UserProfile)

    score = models.IntegerField(default=0)
    previous_score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, 
        force_update=False, **kwargs):
        #acquire global lock on ratings
        commprod_lock.acquire()
        diff = int(self.score) - int(self.previous_score)
        self.previous_score = self.score;
        super(Rating, self).save(force_insert, force_update)
        self.commprod.update_score(diff)
        #release, commprod and user profile are updated by above line
        commprod_lock.release() 

    def __unicode__(self):
    	return """%(username)s voted a %(score)s on 
        commprod_id %(id)s on %(date)s.""" % {
            'username' : self.user_profile.username(), 
            'score' : self.score, 
            'id' : self.commprod.id,
            'date' :  self.date,
        }

class TrendData(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    date = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    avg_score = models.FloatField(default=0.0)

    def __unicode__(self):
        return """%(username)s had a score of %(score)s 
        and avg score of %(avg_score)s on %(date)s.""" % {
            'username' : self.user_profile.username(), 
            'score' : self.score, 
            'avg_score' : self.avg_score, 
            'date' : self.date,
        }

class Correction(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    commprod = models.ForeignKey(CommProd)

    date = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    used = models.BooleanField(default=False)

    def update_score(self, diff, rating_user):
        self.score = self.score + diff
        self.user_profile.score = self.user_profile.score + diff #update user for points
        if rating_user.is_staff and diff >= 0:
            self.use_correction()

        elif self.score == -5:
            self.is_active = False

        elif self.score == 5:
            self.use_correction()

        self.save()

    def use_correction(self, save=False):
        Correction.objects.filter(
            commprod=self.commprod).update(is_active=False)
        self.is_active = False
        self.used = True

        self.commprod.content = self.content
        self.commprod.media_content = urlize_text(self.content)
        self.commprod.media = commprod_contains_media(
            self.content)
        self.commprod.save()
        if save:
            self.save() ##normally called at the end of update_score

    def __unicode__(self):
        return """Correction by %(username)s with content
         %(content)s on %(date)s.""" % {
            "username" : self.user_profile.username(), 
            "content" : self.content, 
            "date" : self.date,
        }

class CorrectionRating(models.Model):
    correction = models.ForeignKey(Correction)
    user_profile = models.ForeignKey(UserProfile)

    previous_score = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False,
         **kwargs):
        correction_lock.acquire()
        diff = int(self.score) - int(self.previous_score)
        self.previous_score = self.score
        super(CorrectionRating, self).save(force_insert, 
            force_update)
        self.correction.update_score(diff, 
            self.user_profile.user)
        correction_lock.release()

    def __unicode__(self):
        return """%(username)s voted a %(score)s 
        on correction_id %(id)s on %(date)s.""" % {
            'username' : self.user_profile.username(), 
            'score' : self.score, 
            'id' : self.correction.id,
            'date' : self.date,
        }

class Favorite(models.Model):
    commprod = models.ForeignKey(CommProd)
    user_profile = models.ForeignKey(UserProfile)

    fav = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return """%(username)s favorited (%(fav)s) the 
        commprod %(id)s on %(date)s.""" % {
            'username' : self.user_profile.username(),
            'fav' : self.fav,
            'id' : self.commprod.id,
            'date' : self.date,
        }

class PasswordReset(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    activation_key = models.CharField(max_length=40, 
        default=get_digest())

    def send_confirm_email(self):
        content = email_templates.forgot_password["content"] \
        % (self.user_profile.user.first_name, 
            "%(base_url)s/reset_password/%(activation_key)s/" % {
                'base_url' : settings.BASE_URL_PROD,
                'activation_key' : self.activation_key,
            })
        subject = email_templates.forgot_password["subject"]
        emails = [self.user_profile.user.email]
        utils.email_users(subject, content, emails)

    def is_valid(self):
        now = timezone.make_aware(datetime.now(), 
            timezone.get_default_timezone())
        time_threshold = now - timedelta(hours=24)
        return self.date_created > time_threshold

    def get_new_passwd(self):
        get_rand = lambda : random.randint(1, 333)
        user = self.user_profile.user
        start = get_rand()
        end = get_rand()
        password = "%(start)s%(username)s%(end)s" % {
            'start' : start,
            'username' : self.user_profile.username(),
            'end' : end, 
            }
        user.set_password(password)
        user.save()
        return password

    def __unicode__(self):
        return """Password reset request by %(username)s 
        on %(date_created)s.""" % {
            'username' : self.user_profile.username(),
            'date_created' : self.date_created,
        }

class CommProdRec(models.Model):
    user_profile = models.ForeignKey(UserProfile)

    ranked_list = models.TextField()

    def get_prods(self, limit=None):
        #annoying hack to get a query set of commprods 
        #in the order of the ranked_list
        pk_list = json.loads(self.ranked_list)
        ordering = "FIELD(`id`, %s)" % \
        ",".join(str(id) for id in pk_list)
        queryset = CommProd.objects.filter(
            pk__in=pk_list).extra(
            select={ "ordering" : ordering }, 
            order_by=("ordering",))
        return queryset


#fuck.
import signals
signals.setup()
