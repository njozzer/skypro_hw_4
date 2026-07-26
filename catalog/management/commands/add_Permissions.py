import json

from django.core.management.base import BaseCommand
from catalog.models import Category
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Команда добавления разрешений"

    def handle(self, *args, **options):
        product_moderator = Group.objects.create(name='Product Moderator')
        can_unpublish_product = Permission.objects.get(codename='can_unpublish_product')
        can_delete_products = Permission.objects.get(codename='delete_product')
        product_moderator.permissions.add(can_unpublish_product, can_delete_products)

