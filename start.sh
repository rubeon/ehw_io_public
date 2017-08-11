DJANGO_DB_ENGINE="django.db.backends.sqlite3" 
DJANGO_DB_NAME="dbname.db" 
DJANGO_DB_USER="db username goes here" 
DJANGO_DB_PASSWORD="password goes here" 
DJANGO_DB_HOST="db_ip_or_hostname" 
DJANGO_DB_PORT="" 
DJANGO_LANG="en-us" 
DJANGO_TIMEZONE="UTC" 
DJANGO_STATIC_URL="/static/" 
DJANGO_SECRET_KEY="asdfasdfasdf"

export DJANGO_SECRET_KEY DJANGO_DB_ENGINE DJANGO_DB_NAME DJANGO_DB_USER DJANGO_DB_PASSWORD DJANGO_DB_HOST DJANGO_DB_PORT DJANGO_LANG DJANGO_TIMEZONE DJANGO_STATIC_URL
uwsgi_python \
        --pythonpath /srv/subc/ehw_io_public/ \
        --socket 0.0.0.0:8001 \
        --module ehw_io_public.wsgi \
        --logdate \
        --optimize 2 \
        --processes 2 \
        --master \
        --enable-threads \
        --single-interpreter \
        --logto /srv/subc/uwsgi.log