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

from django.utils.translation import gettext as _
from rest_framework.exceptions import NotFound

from apps.users.models import User


def get_user(user_id: int) -> User:
    """Get an user by its ID. If the user does not exist in the
    database, raise a :class:`rest_framework.exceptions.NotFound`
    exception.

    Parameters
    ----------
    user_id: :class:`int`
        The ID of the user to get.

    Returns
    -------
    :class:`apps.users.models.User`
        The user with the given ID.

    Raises
    ------
    :class:`rest_framework.exceptions.NotFound`
        If the user does not exist in the database.
    """
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist as exc:
        raise NotFound(_("User not found.")) from exc
