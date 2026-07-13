from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("home/", views.ProductListView.as_view(), name="home"),
    path("product/<int:pk>/",views.ProductDetailView.as_view(), name="product"),
    path("contacts/", views.ContactView.as_view(), name="contacts"),
]

