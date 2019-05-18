#!/bin/bash

HOME="/user/pi/api"
PIDFILE="$HOME/rest_server.pid"
# echo $PIDFILE

if [ -e "${PIDFILE}" ] && (ps -u $(whoami) -opid= | grep -P "^\s*$(cat ${PIDFILE})$" &> /dev/null); then
  # "rest_server.py is already running."
  # echo "already running"
  exit 99
fi

# echo "starting restserver"
/usr/bin/rest_server.py -msc
