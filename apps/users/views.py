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

from typing import TYPE_CHECKING

from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from apps.users.models import User
from apps.users.serializers import CreateUserSerializer

if TYPE_CHECKING:
    UserGenericViewSet = GenericViewSet[User]
else:
    UserGenericViewSet = GenericViewSet


class CreateUserView(CreateModelMixin, UserGenericViewSet):
    """A viewset for creating users."""

    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer
