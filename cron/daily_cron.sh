#! /bin/bash

cd /home/commprod/commprod 
source venv/bin/activate

python manage.py update_trend_data

#update production 
#git checkout master
#python manage.py update_user_list
#git commit -am "dailycron: update to user_list"

git pull heroku master
#git push heroku master
#git push git master

DATE=$(date +"%m-%d-%Y")
#backup database
mysqldump -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_NAME | gzip > "sql_dump/backup-"$DATE.sql.gz 

#cleanup old files
find sql_dump -type f -mtime +30 -exec rm '{}' \;