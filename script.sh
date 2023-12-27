#!/bin/bash
python manage.py makemigrations sales_app
python manage.py migrate
python manage.py loaddata initial_data.json
uwsgi --http :80 --processes 2 --static-map /static=/static --module autocompany.wsgi:application

