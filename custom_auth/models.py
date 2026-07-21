from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=15, help_text='Необязательное поле. Введите ваш номер телефона.')
    country = models.CharField(max_length=40, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['avatar', 'phone', 'country']
    objects = CustomUserManager()

    def __str__(self):
        return self.email
