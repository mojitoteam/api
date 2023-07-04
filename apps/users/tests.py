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

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APITestCase


class SelfUserTestCase(APITestCase):
    """Test case for the current user endpoint."""

    def setUp(self) -> None:
        self.url = reverse("users:self-user-list")
        self.data = {
            "username": "user",
            "email": "user@email.com",
            "password": "password",
        }

    def test_create_user_sucessfully(self) -> None:
        res = self.client.post(self.url, self.data)

        self.assertEqual(res.status_code, HTTP_201_CREATED)
        self.assertDictEqual(res.data, {})
