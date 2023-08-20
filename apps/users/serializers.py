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

from typing import Dict

from rest_framework.serializers import CharField, EmailField, ModelSerializer
from rest_framework.validators import UniqueValidator

from apps.users.models import User


class SelfUserSerializer(ModelSerializer[User]):
    """Serializer for the current user."""

    username = CharField(
        min_length=3,
        max_length=32,
        write_only=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    email = EmailField(
        max_length=256,
        write_only=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = CharField(min_length=8, max_length=128, write_only=True)
    token = CharField(max_length=256, read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]

    def create(self, validated_data: Dict[str, str]) -> User:
        return User.objects.create_user(**validated_data)


class UserSerializer(ModelSerializer[User]):
    """Serializer for the users."""

    class Meta:
        model = User
        fields = ["id", "username", "created_at"]
        read_only_fields = fields
