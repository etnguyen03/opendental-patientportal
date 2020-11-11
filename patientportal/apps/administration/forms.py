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

from django import forms
from localflavor.us.forms import USSocialSecurityNumberField


class NewUserForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email Address", max_length=100)


class ManageUserForm(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=100)


class ResetPasswordForm(forms.Form):
    checkbox = forms.BooleanField(label="Check this box to confirm", required=True)


class Disable2FAForm(forms.Form):
    checkbox = forms.BooleanField(label="Check this box to confirm", required=True)


class AddPatientForm(forms.Form):
    ssn = USSocialSecurityNumberField(label="Patient SSN", required=True)
