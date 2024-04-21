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

from django.conf import settings
from itsdangerous import BadSignature, URLSafeTimedSerializer
from rest_framework.authentication import (
    BaseAuthentication,
    get_authorization_header,
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from apps.users.models import User


class TokenAuthentication(BaseAuthentication):
    """This class is responsible for authenticating an user."""

    header_prefix = "Bearer"

    def authenticate(self, request: Request) -> tuple[User, str] | None:
        auth_header = get_authorization_header(request).split()

        if not auth_header or len(auth_header) != 2:
            return None

        prefix = auth_header[0].decode("utf-8")
        token = auth_header[1].decode("utf-8")

        if prefix != self.header_prefix:
            return None

        return self.validate_token(token)

    def authenticate_header(self, request: Request) -> str:
        return self.header_prefix

    def validate_token(self, token: str) -> tuple[User, str]:
        serializer = URLSafeTimedSerializer(settings.SECRET_KEY, salt="auth")

        try:
            user_id = serializer.loads(token)
            user = User.objects.get(id=user_id)
        except (BadSignature, User.DoesNotExist) as exc:
            raise AuthenticationFailed() from exc

        return (user, token)
