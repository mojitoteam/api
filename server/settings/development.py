"""
Copyright (C) 2023 Mojito Team

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

from server.settings.base import *

######################
#  General Settings  #
######################

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    # Since we have an app running on Heroku, we need to add the
    # Heroku app domain to the list of allowed hosts, otherwise
    # Django will throw an exception when we try to access the
    # app on Heroku.
    ".herokuapp.com",
]

# In development, we don't need a secure password hasher. We can use
# MD5 instead, this is because we don't need to worry about security
# in development. However, we should use a secure password hasher in
# production, like PBKDF2 or Argon2.

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

#########################
#  Django CORS Headers  #
#########################

CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
