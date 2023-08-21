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

from typing import Optional, Tuple

from django.conf import settings
from django.utils.translation import gettext as _
from itsdangerous import BadSignature, URLSafeTimedSerializer
from rest_framework.authentication import (
    BaseAuthentication,
    get_authorization_header,
)
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from apps.users.models import User


class TokenAuthentication(BaseAuthentication):
    """This class is responsible for authenticating an user using a
    token that is passed in the ``Authorization`` header of the request.

    The token must be prefixed with ``Token`` and must be separated from
    the prefix by a space. For example:

    ```txt
    Authorization: Token <token>
    ```
    """

    header_prefix = "Token"

    def authenticate(self, request: Request) -> Optional[Tuple[User, str]]:
        """This method is called on every request, regardless of whether
        the endpoint requires authentication

        This method can return two possible values:

        1) ``None`` is returned if the request does not contain a valid
        token. In this case, the request will be processed as an
        unauthenticated request.

        2) Tuple[:class:`apps.users.model.User`, :class:`str`] is
        returned when the authentication was sucessful. Where this tuple
        is a pair of the user that was authenticated and the token that
        was used to authenticate the user.

        If neither of these two cases were met, that means there was an
        error. In the event of an error, we do not return anything. We
        simple raise the
        :class:`rest_framework.exceptions.AuthenticationFailed`
        exception and let Django REST Framework handle the rest.
        """
        auth_header = get_authorization_header(request).split()

        if not auth_header or len(auth_header) != 2:
            return None

        prefix = auth_header[0].decode("utf-8")
        token = auth_header[1].decode("utf-8")

        if prefix != self.header_prefix:
            return None

        return self.validate_token(token)

    def authenticate_header(self, request: Request) -> str:
        """This method is called when the client does not provide a
        valid token in the `Authorization` header of the request.

        This method returns a string that is sent to the client as the
        value of the ``Authorization`` header. This header tells the
        client what type of authentication is required and how to
        authenticate.

        Parameters
        ----------
        request: :class:`rest_framework.request.Request`
            The request that was made.

        Returns
        -------
        :class:`str`
            The value of the ``Authorization`` header. Always returns
            ``Token``.
        """
        return self.header_prefix

    def validate_token(self, token: str) -> Tuple[User, str]:
        """Validate the given token and return the user that the token
        belongs to. If the token is invalid or the user does not exist,
        then an exception is raised.

        Parameters
        ----------
        token: :class:`str`
            The token to validate.

        Returns
        -------
        tuple[:class:`apps.users.models.User`, :class:`str`]
            A tuple containing the user that the token belongs to and
            the token itself.

        Raises
        ------
        :class:`rest_framework.exceptions.ValidationError`
            Raised when the token is invalid or the user does not exist.
        """
        serializer = URLSafeTimedSerializer(settings.SECRET_KEY, salt="auth")

        try:
            user_id = serializer.loads(token)
            user = User.objects.get(id=user_id)
        except (BadSignature, User.DoesNotExist) as exc:
            raise ValidationError({"detail": _("Invalid token.")}) from exc

        return (user, token)
