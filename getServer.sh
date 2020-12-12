#!/bin/sh
# run using: sudo bash getServer.sh

# make the directories and get all the files
# git clone seems to require my username and password
cd ~/.
mkdir api
cd ~/api/.

wget https://raw.githubusercontent.com/dumbo25/restful_api/master/README.md
wget https://github.com/dumbo25/restful_api/blob/master/favicon.png
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/get.json
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/get.txt
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/rest_server.py
wget https://raw.githubusercontent.com/dumbo25/restful_api/master/server_cron.sh

mkdir cpu
cd ~/api/cpu/.
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/cpu/get.backup
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/cpu/get.json
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/cpu/get.py
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/cpu/get.txt

cd ~/api
mkdir disk
cd ~/api/disk/.
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/disk/get.backup
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/disk/get.json
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/disk/get.py
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/disk/get.txt

cd ~/api
mkdir memory
cd ~/api/memory/.
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/memory/get.backup
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/memory/get.json
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/memory/get.py
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/memory/get.txt

cd ~/api
mkdir os
cd ~/api/os/.
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/os/get.backup
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/os/get.json
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/os/get.py
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/os/get.txt

cd ~/api
mkdir reboot
cd ~/api/reboot/.
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/reboot/get.backup
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/reboot/get.json
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/reboot/get.py
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/reboot/get.txt

cd ~/api
mkdir time
cd ~/api/time/.
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/time/get.backup
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/time/get.json
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/time/get.py
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/time/get.txt

cd ~/api
mkdir uptime
cd ~/api/uptime/.
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/uptime/get.backup
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/uptime/get.json
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/uptime/get.py
https://raw.githubusercontent.com/dumbo25/restful_api/master/server/uptime/get.txt

