from .models import Product, Category
from django.core.cache import cache
class CatalogService:
    @staticmethod
    def get_products_by_category(category_id):

        key = f"category_products_{category_id}"
        product_list = cache.get(key)
        if product_list is not None:
            return product_list
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, 60*60*24)
        return products