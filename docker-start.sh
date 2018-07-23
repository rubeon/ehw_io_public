#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Loading fixtures"
python manage.py load_sample_data --filename=tests/fixtures/test.yaml &> /dev/null
python manage.py rebuild_index --noinput
# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
