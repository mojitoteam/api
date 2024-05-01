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

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, CharField, EmailField

from apps.users.managers import UserManager
from apps.users import serializer
from core.models import TimestampedModel


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    """Represents an user."""

    id: int

    email = EmailField(db_index=True, max_length=80, unique=True)
    username = CharField(db_index=True, max_length=20, unique=True)
    password = CharField(max_length=120)

    # When a user no longer wishes to use our platform, they may try to
    # delete there account. That's a problem for us because the data we
    # collect is valuable to us and we don't want to delete it. To solve
    # this problem, we will simply offer users a way to deactivate their
    # account instead of letting them delete it. That way they won't
    # show up on the site anymore, but we can still analyze the data.
    is_active = BooleanField(default=True)

    # Telling Django that the email field should be used for
    # authentication instead of the username field.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        db_table = "users"

    @property
    def token(self) -> str:
        """Creates a token for the user. This token is used to verify
        the user authenticity when they make requests to the API, which
        is sent in the authorization header.

        Returns
        -------
        :class:`str`
            A token for the user.
        """
        return serializer.dumps(self.id)
