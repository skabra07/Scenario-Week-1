#!/bin/sh
# put the following code in /ect/rc.local
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install libmysqlclient-dev
sudo apt-get install git
git clone -branch deployment https://github.com/skabra07/Scenario-Week-1.git
cd Scenario-Week-1
sudo pip3 install -r requirements.txt
sudo iptables -t nat -A PREROUTING -i eht0 -p tcp --dport 80 -j REDIRECT --to-port 8000
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
