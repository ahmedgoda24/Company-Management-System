
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _
from common.models import TimeStampedModel
from.managers import UserManager
from .choices import UserRole

class User(AbstractUser,TimeStampedModel):
    first_name = models.CharField( max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField( unique=True, db_index=True)
    username = models.CharField(max_length=60, unique=True)
    role = models.CharField(
        max_length=10,
        choices= UserRole.choices,
        default=UserRole.EMPLOYEE,
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()


    @property
    def get_full_name(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()