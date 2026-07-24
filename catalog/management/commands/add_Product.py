import json

from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Команда добавления продуктов"

    def handle(self, *args, **options):
        Product.objects.all().delete()

        with open('product_fixture.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        for product in products:
            product["fields"]['category'] = Category.objects.get(pk=product["fields"]['category'])
            product, created = Product.objects.get_or_create(**product["fields"])
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))

