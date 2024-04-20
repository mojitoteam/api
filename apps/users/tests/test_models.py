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

from apps.users.models import User


class TestUserModelFieds:
    """Test the fields of the user model."""

    def test_username_field_is_email(self) -> None:
        assert User.USERNAME_FIELD == "email"

    def test_required_fields(self) -> None:
        assert User.REQUIRED_FIELDS == ["username"]
