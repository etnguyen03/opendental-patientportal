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

from diceware import get_passphrase
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.management import call_command
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from two_factor.utils import default_device

from ...utils.opendental_db import get_connection, lookup_patient
from ..users.models import Patient
from .forms import (
    AddPatientForm,
    Disable2FAForm,
    ManageUserForm,
    NewUserForm,
    ResetPasswordForm,
)


@user_passes_test(lambda u: u.is_superuser)
@login_required
def administration_view(request):
    context = {
        "newuser_form": NewUserForm(),
        "manageuser_form": ManageUserForm(),
    }
    return render(request, "administration/index.html", context)


@user_passes_test(lambda u: u.is_superuser)
@login_required
def create_new_user_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            get_user_model().objects.create_user(
                username=form.cleaned_data["email"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            messages.success(
                request, f"User {form.cleaned_data['email']} created successfully."
            )
            return redirect(
                "administration:manageuser", user=form.cleaned_data["email"]
            )
        else:
            messages.error(request, "Form invalid.")
            return redirect("administration:index")
    else:
        return HttpResponseBadRequest()


@user_passes_test(lambda u: u.is_superuser)
@login_required
def manage_user_view(request, user):
    user_object = get_object_or_404(get_user_model(), username=user)
    patients = list(Patient.objects.filter(user=user_object))
    context = {
        "username": user_object.username,
        "user_id": user_object.id,
        "reset_password_form": ResetPasswordForm(),
        "attributes": [
            {"key": "First Name", "value": user_object.first_name},
            {"key": "Last Name", "value": user_object.last_name},
            {"key": "Last Login", "value": user_object.last_login},
            {"key": "Signup Time", "value": user_object.date_joined},
            {"key": "Administrator", "value": user_object.is_superuser},
            {"key": "Account Enabled", "value": user_object.is_active},
        ],
        "patients": patients,
        "twofa": default_device(user_object),
        "disable_2fa_form": Disable2FAForm(),
        "addpatient_form": AddPatientForm(),
    }
    return render(request, "administration/manage_user.html", context)


@user_passes_test(lambda u: u.is_superuser)
@login_required
def manage_user_loader_view(request):
    if request.method == "POST":
        form = ManageUserForm(request.POST)
        if form.is_valid():
            try:
                get_user_model().objects.get(username=form.cleaned_data["email"])
            except get_user_model().DoesNotExist:
                messages.error(request, "Invalid user.")
                return redirect("administration:index")
            return redirect(
                "administration:manageuser", user=form.cleaned_data["email"]
            )
        else:
            messages.error(request, "Invalid user.")
            return redirect("administration:index")
    else:
        return HttpResponseBadRequest()


@user_passes_test(lambda u: u.is_superuser)
@login_required
def reset_user_password(request, user: str = None):
    if user is None:
        return HttpResponseBadRequest()
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user_object = get_object_or_404(get_user_model(), username=user)
            new_password = get_passphrase()
            user_object.set_password(new_password)
            user_object.save()
            context = {
                "password": new_password,
                "email_address": user_object.username,
            }
            return render(request, "user_info_printout.html", context)
        else:
            messages.error(request, "Please check the box to confirm reset.")
            return redirect("administration:manageuser", user=user)
    else:
        return HttpResponseBadRequest()


@user_passes_test(lambda u: u.is_superuser)
@login_required
def disable_2fa(request, user: str = None):
    if user is None:
        return HttpResponseBadRequest()
    if request.method == "POST":
        form = Disable2FAForm(request.POST)
        if form.is_valid():
            user_object = get_object_or_404(get_user_model(), username=user)
            call_command("two_factor_disable", user_object.username)
            messages.success(request, "Two factor authentication disabled.")
        else:
            messages.error(request, "Please check the box to confirm reset.")
        return redirect("administration:manageuser", user=user)
    else:
        return HttpResponseBadRequest()


@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_patient_view(request, user: str):
    if user is None:
        return HttpResponseBadRequest()
    if request.method == "POST":
        form = AddPatientForm(request.POST)
        if form.is_valid():
            user_object = get_object_or_404(get_user_model(), username=user)
            mysql_db_connection = get_connection()
            patient = lookup_patient(mysql_db_connection, form.cleaned_data["ssn"])
            patient.user = user_object
            patient.save()

            messages.success(request, "Patient added.")
        else:
            for error in form.errors.values():
                messages.error(request, error)
        return redirect("administration:manageuser", user=user)
    else:
        return HttpResponseBadRequest()
