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

from pathlib import Path

from server.settings import env

#
# General Settings
#

BASE_DIR = Path(__file__).parent.parent.parent

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-secret-key")

DEBUG = env.bool("DJANGO_DEBUG", default=True)

APPEND_SLASH = False

#
# Internationalization
#

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

#
# Middlewares
#

MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]

#
# Databases
#

DATABASES = {"default": env.db()}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#
# URLs
#

ROOT_URLCONF = "server.urls"

#
# Apps
#

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
]

THIRD_PARTY_APPS = [
    "rest_framework",
]

LOCAL_APPS = [
    "apps.users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

#
# Authentication
#

# The model to use to represent an user.
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-user-model

AUTH_USER_MODEL = "users.User"

# The list of validators that are used to check the strength of user's
# passwords. See Password validation for more details.
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

BASE_VALIDATOR = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{BASE_VALIDATOR}.UserAttributeSimilarityValidator"},
    {"NAME": f"{BASE_VALIDATOR}.MinimumLengthValidator"},
    {"NAME": f"{BASE_VALIDATOR}.CommonPasswordValidator"},
    {"NAME": f"{BASE_VALIDATOR}.NumericPasswordValidator"},
]

#
# Django REST Framework
#

DEFAULT_AUTHENTICATION_CLASSES = [
    "apps.authentication.backend.TokenAuthentication",
]

TEST_REQUEST_DEFAULT_FORMAT = "json"

DEFAULT_AUTHENTICATION_CLASSES = [
    "apps.authentication.backend.TokenAuthentication"
]

REST_FRAMEWORK = {
    "TEST_REQUEST_DEFAULT_FORMAT": TEST_REQUEST_DEFAULT_FORMAT,
    "DEFAULT_AUTHENTICATION_CLASSES": DEFAULT_AUTHENTICATION_CLASSES,
}
