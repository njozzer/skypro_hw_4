from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import CreateView

from custom_auth.forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login_page.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    form_class = CustomAuthenticationForm
    http_method_names = ["get", "post", "options"]



    def get_next_page(self):
        return reverse_lazy('goodbye')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomRegisterView(CreateView):
    template_name = 'register_page.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
