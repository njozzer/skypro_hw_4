from django.core.management.base import BaseCommand
from catalog.models import Product
class Command(BaseCommand):
    help = "Команда добавления продуктов"
    def handle(self, *args, **options):
