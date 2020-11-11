# Copyright (c) 2020 Ethan Nguyen. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    BigIntegerField,
    BooleanField,
    CharField,
    ForeignKey,
    OneToOneField,
)
from localflavor.us.models import USSocialSecurityNumberField


class UserProperties(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    user_locked = BooleanField(default=False)


class Patient(models.Model):
    """Defines a patient."""

    opendental_patient_id = BigIntegerField(primary_key=True, default=0)
    user = ForeignKey(User, on_delete=models.CASCADE)
    ssn = USSocialSecurityNumberField(unique=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
