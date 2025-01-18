from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import uuid
from django.utils import timezone
from django.utils.crypto import get_random_string
from .manager import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=256, null=False)
    last_name = models.CharField(max_length=256, null=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    is_active = models.BooleanField(default=True)
    account_created = models.DateTimeField(default=timezone.now, editable=False)

    enterprise_mode = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def random_string():
        return get_random_string(length=15)

    jwt_auth_token = models.CharField(max_length=15, default=random_string)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password", "first_name"]

    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super().save(*args, **kwargs)
