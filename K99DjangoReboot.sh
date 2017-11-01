#!/bin/sh
# save in /etc/rc0.d folder and then type 'sudo chmod +x K99DjangoReboot.sh'
cd /home/snifflogs/Scenario-Week-1/
sudo iptables -t nat -A PREROUTING -i eht0 -p tcp --dport 80 -j REDIRECT --to-port 8000
python3 manage.py runserver 0.0.0.0:8000
