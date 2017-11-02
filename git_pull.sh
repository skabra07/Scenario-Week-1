#!/bin/sh
# run command chmod -R 777 git_pull.sh
sudo fuser -k 8000/tcp
cd /home/snifflogs/Scenario-Week-1/
sudo git pull
sudo python3 manage.py test
sudo python3 manage.py runserver 0.0.0.0:8000
