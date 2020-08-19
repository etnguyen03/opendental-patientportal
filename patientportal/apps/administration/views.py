from diceware import get_passphrase

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required

from two_factor.utils import default_device

from .forms import NewUserForm, ManageUserForm, ResetPasswordForm, Disable2FAForm


@user_passes_test(lambda u: u.is_superuser)
@login_required
def administration_view(request):
    context = {
        "newuser_form": NewUserForm(),
        "manageuser_form": ManageUserForm(),
    }
    return render(request, 'administration/index.html', context)


@user_passes_test(lambda u: u.is_superuser)
@login_required
def create_new_user_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            get_user_model().objects.create_user(username=form.cleaned_data["email"],
                                                 email=form.cleaned_data["email"],
                                                 first_name=form.cleaned_data["first_name"],
                                                 last_name=form.cleaned_data["last_name"])
            messages.success(request, f"User {form.cleaned_data['email']} created successfully.")
            return redirect("administration:manageuser", user=form.cleaned_data["email"])
        else:
            messages.error(request, "Form invalid.")
            return redirect("administration:index")
    else:
        return HttpResponseBadRequest()


@user_passes_test(lambda u: u.is_superuser)
@login_required
def manage_user_view(request, user):
    user_object = get_object_or_404(get_user_model(), username=user)
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
        "twofa": default_device(user_object),
        "disable_2fa_form": Disable2FAForm(),
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
            return redirect("administration:manageuser", user=form.cleaned_data["email"])
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
    if request.method == 'POST':
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
