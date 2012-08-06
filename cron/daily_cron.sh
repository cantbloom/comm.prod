#! /bin/bash

cd /home/commprod/commprod 
source venv/bin/activate

#update production and staging
git checkout master
python manage.py update_user_list
python manage.py update_trend_data
git commit -am "update to user_list"

git pull staging master
git push staging master

git push origin master
