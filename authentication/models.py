import datetime
import os
import random
import string
from hashlib import sha256
from typing import Optional, TYPE_CHECKING, Tuple

import pytz
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session
from django.db import models
from django.db.models import IntegerChoices
from django.dispatch import receiver

from common.models import BaseModel, BaseFileModel

class User(AbstractUser):
    """Base User model"""

    first_name = None
    last_name = None

    # Names
    profile_username = models.CharField("Profile username", max_length=64, null=True, blank=True)

    # Personal
    birth_date = models.DateField("DOB", null=True, blank=True)

    # Contacts
    email = models.EmailField("Email", unique=True, null=True)
    phone = models.CharField("Phone", null=True, max_length=32, blank=True)

    telegram_id = models.BigIntegerField("Telegram ID", null=True, blank=True)
    telegram_username = models.CharField("Telegram Username", max_length=128, unique=True, null=True)

    language_code = models.CharField("Language code", max_length=4, default="ru")

    is_dark_theme = models.BooleanField("Is Dark Theme", default=False)

    is_banned = models.BooleanField("Is Banned", default=False)
    is_paid = models.BooleanField("Is Paid", default=False)

    avatars = models.ManyToOneRel(field="avatars", to="UserAvatar", field_name="user", related_name="avatars")
    user_session = models.ManyToOneRel(field="user_sessions", to="UserSession", field_name="user", related_name="user_session")
    is_account_activated = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []



class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_session")
    session = models.OneToOneField(Session, on_delete=models.CASCADE, related_name="user_session")


class UserAvatar(BaseFileModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="avatars")
    is_active = models.BooleanField("Is Active", default=True)
    is_default = models.BooleanField("Is Default", default=False)


@receiver(models.signals.post_delete, sender=UserAvatar)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=UserAvatar)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False



class UserInteresting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    phone = models.TextField("Description", null=True, blank=True)
    url = models.CharField("Url", null=True, max_length=100, blank=True)

