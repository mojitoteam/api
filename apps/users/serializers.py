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

from typing import TypedDict

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as BaseValidationError
from rest_framework.exceptions import ValidationError

from apps.users.models import User


class UserCreateRequest(TypedDict):
    """Type definition for the request body of the create user endpoint."""

    username: str
    email: str
    password: str


class UserCreateSerializer(ModelSerializer[User]):
    """Serializer for the create user endpoint."""

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]
        extra_kwargs = {
            k: {"write_only": True} for k in fields if k != "token"
        }

    def create(self, validated_data: UserCreateRequest) -> User:
        return User.objects.create_user(**validated_data)

    def validate_password(self, password: str) -> str:
        try:
            validate_password(password)
        except BaseValidationError as exc:
            raise ValidationError({"password": exc.messages}) from exc

        return password


class UserSerializer(ModelSerializer[User]):
    """Serializer for the user model."""

    class Meta:
        model = User
        fields = ["id", "last_login", "created_at", "updated_at", "username"]
