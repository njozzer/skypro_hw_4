from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("home/", views.ProductListView.as_view(), name="home"),
    path("product/<int:pk>/",views.ProductDetailView.as_view(), name="product"),
    path("product/<int:pk>/edit/",views.ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/",views.ProductDeleteView.as_view(), name="product_delete"),
    path("product/new/", views.ProductCreateView.as_view(), name="product_create"),
    path("contacts/", views.ContactView.as_view(), name="contacts"),
]

