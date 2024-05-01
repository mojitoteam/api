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

from django.db.models import CharField, ManyToManyField, DateTimeField
from django.core.exceptions import ValidationError

from core.models import TimestampedModel
from apps.users.models import User


class Contest(TimestampedModel):
    """Represents a contest."""

    title = CharField(max_length=50)
    description = CharField(max_length=200)

    start_date = DateTimeField()
    end_date = DateTimeField()

    participants = ManyToManyField(User, related_name="contests")

    class Meta:
        db_table = "contests"

    def clean(self) -> None:
        if self.start_date > self.end_date:
            raise ValidationError({
                "start_date": "The start date must be before the end date."
            })
