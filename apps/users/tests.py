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
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from rest_framework.test import APITestCase

from apps.users.models import User
from apps.users.serializers import UserSerializer


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
        data = res.data

        expected = {"token": data["token"]}

        self.assertEqual(res.status_code, HTTP_201_CREATED)
        self.assertDictEqual(res.data, expected)


class UsersTestCase(APITestCase):
    """Test case for the users endpoint."""

    def setUp(self) -> None:
        self.example = {
            "username": "user",
            "email": "user@email.com",
            "password": "password",
        }
        self.user = User.objects.create_user(**self.example)

    def test_get_self(self) -> None:
        url = reverse("users:users-detail", kwargs={"pk": "me"})
        self.client.force_authenticate(self.user)

        res = self.client.get(url)
        expected = UserSerializer(self.user)

        self.assertDictEqual(res.data, expected.data)

    def test_get_self_without_authentication(self) -> None:
        url = reverse("users:users-detail", kwargs={"pk": "me"})

        res = self.client.get(url)
        expected = {"detail": "Authentication credentials were not provided."}

        self.assertEqual(res.status_code, HTTP_401_UNAUTHORIZED)
        self.assertDictEqual(res.data, expected)

    def test_get_user(self) -> None:
        url = reverse("users:users-detail", kwargs={"pk": self.user.id})
        self.client.force_authenticate(self.user)

        res = self.client.get(url)
        expected = UserSerializer(self.user)

        self.assertDictEqual(res.data, expected.data)

    def test_get_user_without_authentication(self) -> None:
        url = reverse("users:users-detail", kwargs={"pk": self.user.id})

        res = self.client.get(url)
        expected = {"detail": "Authentication credentials were not provided."}

        self.assertEqual(res.status_code, HTTP_401_UNAUTHORIZED)
        self.assertDictEqual(res.data, expected)
