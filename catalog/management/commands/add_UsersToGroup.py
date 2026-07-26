import json

from django.core.management.base import BaseCommand
from catalog.models import Category
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

from custom_auth.models import CustomUser


class Command(BaseCommand):
    help = "Команда добавления разрешений пользователю"

    def handle(self, *args, **options):

        product_moderator = Group.objects.get(name='Product Moderator')
        user = CustomUser.objects.get(email='asd@asd.ru')
        user.groups.add(product_moderator)

