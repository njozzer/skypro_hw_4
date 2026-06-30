import json

from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    help = "Команда добавления категорий"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        with open('category_fixture.json', 'r', encoding='utf-8') as file:
            categories = json.load(file)
        for category in categories:
            category, created = Category.objects.get_or_create(**category.get('fields', {}))
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added category: {category.name}'))

