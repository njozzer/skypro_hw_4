from django.db import models
from custom_auth import models as custom_auth_models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории', blank=True, null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.TextField(verbose_name='Описание продукта', blank=True, null=True)
    picture = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True)
    is_publicated = models.BooleanField(verbose_name='признак публикац', default=False)
    owner = models.ForeignKey(custom_auth_models.CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name', 'description']
        permissions = [('can_unpublish_product', 'Can unpublish product'),
                       ('can_delete_products', 'Can delete product'), ]

    def __str__(self):
        return self.name
