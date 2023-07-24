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

from rest_framework.routers import SimpleRouter

from apps.users.views import SelfUserView

app_name = "users"

router = SimpleRouter(trailing_slash=False)
router.register(r"users", SelfUserView, basename="self-user")

urlpatterns = router.urls
