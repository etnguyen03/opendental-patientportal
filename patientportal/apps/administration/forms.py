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

