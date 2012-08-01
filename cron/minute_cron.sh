#! /bin/bash

cd /home/commprod/commprod

source venv/bin/activate 
python cron/parseprod_cron.py 
python manage.py update_trends