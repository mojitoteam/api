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

from os.path import join
from pathlib import Path

from environ import Env

BASE_DIR = Path(__file__).parent.parent.parent

# Load environment variables from config/.env file. See
# https://django-environ.readthedocs.io/en/latest/

env = Env()
env.read_env(join(BASE_DIR, "config", ".env"))
