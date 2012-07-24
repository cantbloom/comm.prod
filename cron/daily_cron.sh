#! /bin/bash

cd /home/cantbloom/commprod 
source venv/bin/activate

#update production
git checkout master
python manage.py updateTrends
git commit -am "update to user_list"
git pull origin master
git push origin master

#update staging
git checkout staging
python manage.py updateTrends
git commit -am "update to user_list"
git pull staging master
git push staging master