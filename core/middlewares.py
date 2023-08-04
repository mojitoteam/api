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

from typing import Callable

from django.http import HttpRequest, HttpResponse


class RemoveHeaders:
    """Middleware to remove some headers from the response."""

    def __init__(
        self, get_response: Callable[[HttpRequest], HttpResponse]
    ) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)

        del response["Allow"]
        del response["Vary"]
        del response["X-Frame-Options"]
        del response["X-Content-Type-Options"]
        del response["Referrer-Policy"]
        del response["Cross-Origin-Opener-Policy"]

        return response
