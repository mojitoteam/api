#!/bin/bash

# This script creates a .env file in the config directory and
# generates a random secret key for the Django app automatically.

read -r -d '' SECRET_KEY_CMD << EOF
from django.utils.crypto import get_random_string;
print(get_random_string(64))
EOF

SECRET_KEY=$(python3 -c "${SECRET_KEY_CMD}")
OUTPUT=$(sed "s/^\(DJANGO_SECRET_KEY=\).*/\1$SECRET_KEY/" .env.example)

echo "$OUTPUT" > .env
echo "=> .env file created successfully!"
