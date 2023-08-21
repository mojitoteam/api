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

from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from apps.users.models import User
from apps.users.serializers import SelfUserSerializer, UserSerializer
from apps.users.utils import get_user

if TYPE_CHECKING:
    UserGenericViewSet = GenericViewSet[User]
else:
    UserGenericViewSet = GenericViewSet


class SelfUserView(CreateModelMixin, UserGenericViewSet):
    """View for the current user."""

    permission_classes = [AllowAny]
    serializer_class = SelfUserSerializer


class UsersView(RetrieveModelMixin, UserGenericViewSet):
    """View for user objects."""

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        pk = kwargs.pop("pk")
        # If the user is requesting their own data (/users/me), then
        # we will return the data of the authenticated user.
        target = request.user if pk == "me" else get_user(pk)

        serializer = self.get_serializer(target)
        return Response(serializer.data, status=HTTP_200_OK)
