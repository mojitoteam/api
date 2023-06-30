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

from server.settings.development import *

###############
#  Databases  #
###############

# Since we are in a CI environment, we don't want to use the default
# database. PostgreSQL is too heavy for a CI environment, so we use
# SQLite instead.

DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3"}
