from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=15, help_text='Необязательное поле. Введите ваш номер телефона.')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['avatar', 'phone']
    def __str__(self):
        return self.email