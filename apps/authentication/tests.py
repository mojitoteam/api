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

from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from apps.users.models import User


class LoginTestCase(APITestCase):
    """Test case for the login endpoint."""

    def setUp(self) -> None:
        self.example = {"email": "user@email.com", "password": "test"}
        self.url = reverse("authentication:login")
        self.user = User.objects.create_user(**self.example, username="user")

    def test_login_user_successfully(self) -> None:
        response = self.client.post(self.url, self.example)
        expected = {"token": self.user.token}

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertDictEqual(response.data, expected)
