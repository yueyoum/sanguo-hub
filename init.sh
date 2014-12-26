#!/bin/bash

for i in `ls hub_fixtures`
do
echo $i
python manage.py loaddata $i
done

python manage.py loadconfig store
