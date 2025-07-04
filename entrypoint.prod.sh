#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    DJANGO_ALLOWED_HOSTS
    
    echo "PostgreSQL started"
fi

exec "$@"