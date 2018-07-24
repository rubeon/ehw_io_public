#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
echo "Loading fixtures"
# python manage.py load_sample_data --filename=tests/fixtures/test.yaml &> /dev/null
python manage.py rebuild_index --noinput

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DJANGO_ADMIN_USER:-admin}', '${DJANGO_ADMIN_EMAIL:-admin@example.com}', '${DJANGO_ADMIN_PASSWORD:-password}')" | python manage.py shell

# Start server
echo "Starting server"
# python manage.py runserver 0.0.0.0:8000
uwsgi \
    --home /usr/local/ \
    --socket 0.0.0.0:8000 \
    --module ehw_io_public.wsgi \
    --logdate \
    --optimize 2 \
    --processes 2 \
    --master \
    --enable-threads \
    --single-interpreter \
    --logto uwsgi.log \
    --die-on-term

sleep 600
