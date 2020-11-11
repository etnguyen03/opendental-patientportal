from django.db import models
from django.contrib.auth.models import User
from django.db.models import BooleanField, ForeignKey, CharField, OneToOneField, BigIntegerField
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

