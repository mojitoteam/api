#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

# We need this line to make sure that this container
# is started after the one with PostgreSQL:
echo "=> Waiting for PostgreSQL to be ready..."
dockerize -wait "tcp://$POSTGRES_HOST:$POSTGRES_PORT" -timeout 90s

echo "=> Executing migrations..."
python manage.py migrate

exec "$@"
