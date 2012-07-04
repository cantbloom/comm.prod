from boto.s3.connection import S3Connection
from boto.s3.key import Key

from commProd.models import UserProfile
from commerical_production.config import AWS
from urllib import urlretrieve

import md5, os


"""
Takes a url from filepicker and uploads
it to our aws s3 account.
"""
def put_profile_pic(url, profile):
    filename, headers = urlretrieve(url)
    conn = S3Connection(AWS['aws_access_key_id'], AWS['aws_secret_access_key'])
    b = conn.get_bucket(AWS['bucket'])
    k = Key(b)
    k.key = md5.new(profile.user.username).hexdigest()
    k.set_contents_from_filename(filename) 
    
    #update user profile
    return "http://s3.amazonaws.com/%s/%s"% (AWS['bucket'], k.key)

