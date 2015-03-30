#!/bin/bash

python manage.py loaddata package.json
python manage.py loaddata package_hero.json
python manage.py loaddata package_soul.json
python manage.py loaddata package_equipment.json
python manage.py loaddata package_gem.json
python manage.py loaddata package_stuff.json
python manage.py loaddata checkin_date.json
python manage.py loaddata checkin_item.json
python manage.py loaddata store.json

python manage.py loadconfig store
