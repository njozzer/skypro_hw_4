from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('home')