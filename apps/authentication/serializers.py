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

from typing import TypedDict, cast

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import Serializer
from rest_framework.fields import EmailField, CharField

from apps.users.models import User


class LoginRequest(TypedDict):
    """Type definition for the request body of the login endpoint."""

    email: str
    password: str


class LoginResponse(TypedDict):
    """Type definition for the response body of the login endpoint."""

    token: str


class LoginSerializer(Serializer[LoginRequest]):
    """Serializer for logging in an user."""

    email = EmailField(max_length=80, write_only=True, required=True)
    password = CharField(
        min_length=8, max_length=120, write_only=True, required=True
    )
    token = CharField(read_only=True)

    def validate(self, attrs: LoginRequest) -> LoginResponse:
        user = cast(User | None, authenticate(**attrs))

        if user is None or not user.is_active:
            raise AuthenticationFailed()

        return {"token": user.token}
