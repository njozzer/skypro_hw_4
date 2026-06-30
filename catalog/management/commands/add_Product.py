from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Команда добавления продуктов"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        category, _ = Category.objects.get_or_create(name='Категория 1')
        products = [
            {"name": "Продукт 1", "description": "Описание продукта 1", "category": category, "price": 2345},
            {"name": "Продукт 2", "description": "Описание продукта 2", "category": category, "price": 2345}
        ]
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))

