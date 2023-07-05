from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomBaseManager


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    is_assistant = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    cus_id = models.CharField(
        max_length=200, null=True, unique=True
    )  # ? This may be used for Stripe accounts

    objects = CustomBaseManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class BaseUser(models.Model):
    location = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Assistant(models.Model):
    IDENTITY = [
        ("NIN", "NIN"),
        ("Passport", "Passport"),
        ("VIN", "Voters Card"),
    ]

    age = models.PositiveSmallIntegerField(null=True)
    bio = models.CharField(max_length=500, null=True)
    passport = models.URLField(null=True)

    services = models.JSONField(help_text="list of services", default=list)
    qualifications = models.CharField(max_length=500, null=True)
    id_card = models.CharField(max_length=500, choices=IDENTITY, null=True)
    id_card_number = models.CharField(max_length=200, null=True)
    height = models.PositiveSmallIntegerField(help_text="in centimeters", null=True)
    disability = models.BooleanField(default=False, null=True)
    allergy = models.CharField(max_length=200, null=True, blank=True)
    experience = models.PositiveSmallIntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
