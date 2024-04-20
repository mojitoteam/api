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

from typing import TYPE_CHECKING, Any

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

if TYPE_CHECKING:
    from apps.users.models import User
else:
    User = Any


class UserManager(BaseUserManager[User]):
    """Custom manager for the :class:`apps.users.models.User` model."""

    def create_user(self, username: str, email: str, password: str) -> User:
        """Creates a new user with the given data.

        Parameters
        ----------
        username: :class:`str`
            The user's username.
        email: :class:`str`
            The user's email address.
        password: :class:`str`
            The user's password.

        Returns
        -------
        :class:`apps.users.models.User`
            A new user object with the provided data.
        """
        email = self.normalize_email(email)

        # Run validators on the email and password to make sure they're
        # valid. If they're not, an exception will be raised, but we
        # don't need to catch it because it will be caught by the
        # serializer.
        validate_email(email)
        validate_password(password)

        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()

        return user
