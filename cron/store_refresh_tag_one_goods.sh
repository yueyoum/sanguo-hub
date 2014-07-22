#!/bin/bash
SELF=$(readlink -f $0)
PROJECT_PATH=$(dirname $(dirname $SELF))
cd $PROJECT_PATH

source env/bin/activate


python cron/store_refresh_tag_one_goods.py

exit $?
