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

from typing import cast
from collections.abc import Sequence

from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    BasePermission,
    AllowAny,
    IsAuthenticated,
)

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserCreateSerializer
from apps.users.permissions import OwnerOnly


class UsersViewSet(ModelViewSet[User]):
    """View set for the users endpoint."""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & OwnerOnly]

    # Actions that don't require authentication to be performed.
    public_actions = ["create", "retrieve"]

    def get_permissions(self) -> Sequence[BasePermission]:
        if self.action in self.public_actions:
            return [AllowAny()]

        return cast(Sequence[BasePermission], super().get_permissions())

    def get_serializer_class(self) -> type[BaseSerializer[User]]:
        if self.action == "create":
            return UserCreateSerializer

        return UserSerializer
