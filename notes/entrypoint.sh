#!/bin/sh
# entrypoint.sh

# Run migrations
python manage.py makemigrations
python manage.py migrate

#create superuser
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

# Then run the main container command (passed to us as arguments)
exec "$@"