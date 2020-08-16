from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, ForeignKey, CharField
from localflavor.us.models import USSocialSecurityNumberField


class User(AbstractUser):
    """Defines a user that can log in."""
    user_locked = BooleanField(default=False)


class Patient():
    """Defines a patient."""

    user = ForeignKey(User, on_delete=models.CASCADE)
    identifier = USSocialSecurityNumberField(unique=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)

