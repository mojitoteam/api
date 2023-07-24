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

from django.db.models import DateTimeField, Model


class TimestampedModel(Model):
    """An abstract base class model that provides self-updating fields.
    This is useful for tracking the creation and modification of
    objects. This model is intended to be inherited from, not used
    directly.
    """

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from this class should be
        # ordered in reverse-chronological order. We can override this
        # on a per-model basis as needed, but reverse-chronological is a
        # good default ordering for most models.
        ordering = ["-created_at", "-updated_at"]
