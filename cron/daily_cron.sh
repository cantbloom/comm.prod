#! /bin/bash

cd /home/cantbloom/commprod 
source venv/bin/activate

#update staging
git checkout staging
python manage.py update_trends
python manage.py update_user_list
git commit -am "update to user_list"
git pull staging master
git push staging master


#update production
git checkout master
python manage.py update_trends
python manage.py update_user_list
git commit -am "update to user_list"
git pull origin master
git push origin master
