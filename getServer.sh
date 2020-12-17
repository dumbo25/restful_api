#!/bin/sh
# run using: sudo bash getServer.sh

# make the directories and get all the files
# git clone seems to require my username and password
cd ~/.
mkdir api
cd ~/api/.

wget https://raw.githubusercontent.com/dumbo25/restful_api/master/README.md
wget https://github.com/dumbo25/restful_api/blob/master/favicon.png
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/server_cron.sh

wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/rest_server.py

wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/get.txt

mkdir cpu
cd ~/api/cpu/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/cpu/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/cpu/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/cpu/get.txt

cd ~/api
mkdir disk
cd ~/api/disk/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/disk/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/disk/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/disk/get.txt

cd ~/api
mkdir memory
cd ~/api/memory/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/memory/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/memory/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/memory/get.txt

cd ~/api
mkdir navigation
cd ~/api/navigation/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/navigation/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/navigation/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/navigation/get.txt

cd ~/api
mkdir os
cd ~/api/os/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/os/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/os/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/os/get.txt

cd ~/api
mkdir reboot
cd ~/api/reboot/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/reboot/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/reboot/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/reboot/get.txt

cd ~/api
mkdir time
cd ~/api/time/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/time/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/time/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/time/get.txt

cd ~/api
mkdir uptime
cd ~/api/uptime/.
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/uptime/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/uptime/get.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/api/uptime/get.txt


