import json

from django.core.management.base import BaseCommand
from catalog.models import Category
from django.contrib.auth.models import Permission

class Command(BaseCommand):
    help = "Команда добавления разрешений"

    def handle(self, *args, **options):

        pass
