from django.urls import path

from catalog import views

urlpatterns = [
    path("login/", views.ProductListView.as_view(), name="login"),
    path("logout/", views.ProductListView.as_view(), name="logout"),
    path("register/", views.ProductListView.as_view(), name="register"),
]

