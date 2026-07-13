from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Articles

class ArticlesCreateView(CreateView):
    model = Articles
    fields = ['name', 'description']
    template_name = 'articles_form.html'
    success_url = reverse_lazy('articles_list')

class ArticlesListView(ListView):
    model = Articles
    template_name = 'articles_list.html'
    context_object_name = 'articles'

class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'articles_detail.html'
    context_object_name = 'articles'

class ArticlesUpdateView(UpdateView):
    model = Articles
    fields = ['name', 'description']
    template_name = 'articles_form.html'
    success_url = reverse_lazy('articles_list')
    
class ArticlesDeleteView(DeleteView):
    model = Articles
    template_name = 'articles_confirm_delete.html'
    success_url = reverse_lazy('articles_list')