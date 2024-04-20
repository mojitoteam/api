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


class CreateUserSerializer(ModelSerializer[User]):
    """Serializer for creating users."""

    email = EmailField(
        max_length=80,
        write_only=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This email is already in use.",
            ),
        ],
    )
    username = CharField(
        min_length=2,
        max_length=20,
        write_only=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This username is already in use.",
            ),
        ],
    )
    password = CharField(min_length=8, max_length=128, write_only=True)
    token = CharField(max_length=128, read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]

    def create(self, validated_data: Dict[str, str]) -> User:
        return User.objects.create_user(**validated_data)
