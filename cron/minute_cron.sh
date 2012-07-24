#! /bin/bash

cd /home/cantbloom/commprod

source venv/bin/activate 
python cron/parseprod_cron.py 
python commprod/manage.py updateTrends