from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, phone="", **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, phone="", **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, phone, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=250, unique=True, verbose_name='کاربر')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=250, verbose_name='شماره موبایل')
    activate = models.BooleanField(default=False, verbose_name='فعال بودن یا نبودن کاربر')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email, phone, username]
    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')

