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

if TYPE_CHECKING:
    from apps.users.models import User
else:
    User = Any


class UserManager(BaseUserManager[User]):
    """Custom manager for the :class:`apps.users.models.User` model."""

    def create_user(self, username: str, email: str, password: str) -> User:
        """Creates a new user.

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
        if not username:
            raise ValueError("Users must have an username.")

        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user
