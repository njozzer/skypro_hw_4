from django.contrib.auth.decorators import login_not_required
from django.urls import path

from custom_auth import views

urlpatterns = [
    path("login/", login_not_required(views.CustomLoginView.as_view()), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", login_not_required(views.CustomRegisterView.as_view()), name="register"),
]

