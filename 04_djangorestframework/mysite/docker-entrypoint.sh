#!/bin/bash

dockerize -wait tcp://db:5432 -timeout 20s

# Apply database migrations
echo "Apply database migrations"  
python manage.py migrate

python manage.py makemigrations products
python manage.py migrate

# Start server
echo "Start server" 
python manage.py runserver 0.0.0.0:8000  