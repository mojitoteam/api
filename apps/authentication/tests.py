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

from typing import Tuple, cast

from django.urls import reverse
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIRequestFactory, APITestCase

from apps.authentication.backend import TokenAuthentication
from apps.users.models import User


class LoginTestCase(APITestCase):
    """Test case for the login endpoint."""

    def setUp(self) -> None:
        self.example = {"email": "user@email.com", "password": "password"}
        self.url = reverse("authentication:login")
        self.user = User.objects.create_user(**self.example, username="user")

    def test_login_user_successfully(self) -> None:
        response = self.client.post(self.url, self.example)
        expected = {"token": self.user.token}

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertDictEqual(response.data, expected)


class TokenAuthenticationTestCase(APITestCase):
    """ """

    def setUp(self) -> None:
        self.auth = TokenAuthentication()
        self.url = reverse("authentication:login")

        self.payload = {"email": "user@email.com", "password": "password"}
        self.user = User.objects.create_user(**self.payload, username="user")

        self.factory = APIRequestFactory()

    def test_authentication_with_valid_token(self) -> None:
        res = self.auth.validate_token(self.user.token)
        expected = (self.user, self.user.token)

        self.assertTupleEqual(res, expected)

    def test_authentication_with_invalid_token(self) -> None:
        self.assertRaises(
            ValidationError,
            self.auth.validate_token,
            "invalid_token",
        )

    def test_authentication_with_non_existing_user(self) -> None:
        user = User(
            id=100,
            email="user@email.com",
            username="user",
            password="password",
        )

        self.assertRaises(
            ValidationError, self.auth.validate_token, user.token
        )

    def test_authentication_with_no_header(self) -> None:
        req = self.factory.get(self.url, self.payload)
        self.assertIsNone(self.auth.authenticate(req))

    def test_authentication_with_short_header(self) -> None:
        req = self.factory.get(
            self.url, self.payload, HTTP_AUTHORIZATION="Token"
        )
        self.assertIsNone(self.auth.authenticate(req))

    def test_authentication_with_long_header(self) -> None:
        req = self.factory.get(
            self.url,
            self.payload,
            HTTP_AUTHORIZATION="Token invalid_token invalid_suffix",
        )
        self.assertIsNone(self.auth.authenticate(req))

    def test_authentication_with_invalid_header_prefix(self) -> None:
        req = self.factory.get(
            self.url,
            self.payload,
            HTTP_AUTHORIZATION=f"Invalid {self.user.token}",
        )
        self.assertIsNone(self.auth.authenticate(req))

    def test_authentication_with_valid_header(self) -> None:
        req = self.factory.get(
            self.url,
            self.payload,
            HTTP_AUTHORIZATION=f"Token {self.user.token}",
        )

        res = self.auth.authenticate(req)
        expected = (self.user, self.user.token)

        self.assertIsNotNone(res)
        self.assertTupleEqual(cast(Tuple[User, str], res), expected)
