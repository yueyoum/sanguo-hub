#!/bin/bash
SELF=$(readlink -f $0)
PROJECT_PATH=$(dirname $(dirname $SELF))
cd $PROJECT_PATH

source env/bin/activate


python cron/send_mail.py

exit $?