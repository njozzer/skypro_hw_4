from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("home/", views.home_page, name="home"),
    path("product/<int:pk>/",views.product_page, name="product"),
    path("contacts/", views.contacts, name="contacts"),
]

