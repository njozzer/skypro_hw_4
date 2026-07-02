from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home_page(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, "home.html", context)


def contacts(request):
    return render(request, "contacts.html")
