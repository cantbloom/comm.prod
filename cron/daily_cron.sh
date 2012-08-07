#! /bin/bash

cd /home/commprod/commprod 
source venv/bin/activate

#update production 
git checkout master
python manage.py update_user_list
python manage.py update_trend_data
git commit -am "dailycron: update to user_list"

git pull origin master
git push origin master
