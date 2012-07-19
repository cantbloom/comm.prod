from models import CommProd, Rating, UserProfile, ShirtName
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from helpers.update_user_list import update


def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance) 
       ## updates global javascript variable for user list on base page
       update() 

def post_save_ratings (sender, instance, **kwargs):
    instance.commprod.update_avg()
    instance.commprod.user_profile.update_avg()

def setup():
    post_save.connect(create_user_profile, sender=User) 
    #accomplished by overriding save method # post_save.connect(post_save_ratings, sender=Rating)
