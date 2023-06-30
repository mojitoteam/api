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
from typing import List

from server.settings import BASE_DIR, env

######################
#  General Settings  #
######################

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-secret-key")

DEBUG = env.bool("DJANGO_DEBUG", default=True)

# We don't want to append a slash to the end of URLs, so we disable it.
# This is because we want to use the same URLs schema for both the API
# and the front-end.

APPEND_SLASH = False

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [join(BASE_DIR, "locale")]

#################
#  Middlewares  #
#################

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

###############
#  Databases  #
###############

DATABASES = {"default": env.db()}

##########
#  URLs  #
##########

ROOT_URLCONF = "server.urls"

WSGI_APPLICATION = "server.wsgi.application"

##########
#  Apps  #
##########

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
]

THIRD_PARTY_APPS = [
    "rest_framework",
]

LOCAL_APPS: List[str] = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

####################
#  Authentication  #
####################

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

###############
#  Passwords  #
###############

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# The list of validators that are used to check the strength of user's
# passwords. See Password validation for more details.
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

BASE_PASSWORD_VALIDATOR = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.UserAttributeSimilarityValidator"},
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.MinimumLengthValidator"},
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.CommonPasswordValidator"},
    {"NAME": f"{BASE_PASSWORD_VALIDATOR}.NumericPasswordValidator"},
]

###########################
#  Django REST Framework  #
###########################

DEFAULT_VERSIONING_CLASS = "rest_framework.versioning.URLPathVersioning"

TEST_REQUEST_DEFAULT_FORMAT = "json"

REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": DEFAULT_VERSIONING_CLASS,
    "TEST_REQUEST_DEFAULT_FORMAT": TEST_REQUEST_DEFAULT_FORMAT,
}
