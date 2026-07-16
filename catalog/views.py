from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from catalog.forms import ProductForm
from catalog.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_page.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_new.html'
    success_url = reverse_lazy('home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'product_update_form.html'

    def get_success_url(self):
        return reverse_lazy('product', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('home')


class ContactView(TemplateView):
    template_name = 'contacts.html'
# def home_page(request):
#    product_list = Product.objects.all()
#    context = {'product_list': product_list}
#    return render(request, "home.html", context)


# def contacts(request):
#    return render(request, "contacts.html")

# def product_page(request, pk):
#    product_data = Product.objects.get(pk=pk)
#    context = {'product': product_data}
#    return render(request, "product_page.html", context)
