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

from typing import Optional, TypedDict, cast

from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from rest_framework.exceptions import NotAuthenticated
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import Serializer

from apps.users.models import User


class LoginRequestDict(TypedDict):
    email: str
    password: str


class LoginResponseDict(TypedDict):
    token: str


class LoginSerializer(Serializer[LoginResponseDict]):
    """Serializer for logging in a user."""

    email = EmailField(max_length=256, write_only=True, required=True)
    password = CharField(max_length=128, write_only=True, required=True)
    token = CharField(max_length=256, read_only=True)

    def validate(self, attrs: LoginRequestDict) -> LoginResponseDict:
        email = attrs["email"]
        password = attrs["password"]

        user = cast(
            Optional[User], authenticate(username=email, password=password)
        )

        if user is None or not user.is_active:
            raise NotAuthenticated(
                _("Unable to login with provided credentials.")
            )

        return {"token": user.token}
