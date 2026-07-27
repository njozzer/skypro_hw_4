from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_not_required
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from catalog.services import CatalogService


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        queryset = cache.get('product_list_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('product_list_queryset', queryset, 60 * 15)
        return queryset


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_page.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'product_update_form.html'

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk', 1))
        if product.owner != request.user and not request.user.groups.filter(name='Product moderator').exists():
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('product', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('pk', 1))
        if product.owner != request.user and not request.user.groups.filter(name='Product moderator').exists():
            return HttpResponseForbidden()
        product.delete()
        return redirect('home')


class ContactView(TemplateView):
    template_name = 'contacts.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category_list'


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст данных из родительского класса
        context = super().get_context_data(**kwargs)

        context['product_list'] = CatalogService.get_products_by_category(self.kwargs['pk'])
        return context

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
