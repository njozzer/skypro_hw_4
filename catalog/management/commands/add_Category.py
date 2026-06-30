from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    help = "Команда добавления категорий"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        categories = [
            {"name": "Категория 1", "description": "Описание 1"},
            {"name": "Категория 2", "description": "Описание 2"}
        ]
        for category in categories:
            category, created = Category.objects.get_or_create(**category)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added category: {category.name}'))

