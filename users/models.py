from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "FEMALE"),
        (GENDER_OTHER, "OTHER")
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_TURKISH = "tu"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_TURKISH, "Turkish")
    )

    CURRENCY_USD = "usd"
    CURRENCY_TRY = "try"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_TRY, "TRY")
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    superhost = models.BooleanField(default=False)
