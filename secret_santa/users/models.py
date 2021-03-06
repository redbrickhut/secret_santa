from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):

        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if not kwargs.get("is_staff"):
            raise ValueError("Superuser must be is_staff")
        if not kwargs.get("is_superuser"):
            raise ValueError("Superuser must be is_superuser")

        return self.create_user(email, password, **kwargs)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email", unique=True)
    profile_picture = models.ImageField(upload_to='profiles', null=True, blank=True)
    display_name = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"<User: {self.email}>"
