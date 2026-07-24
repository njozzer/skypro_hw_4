from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Articles

class ArticlesCreateView(CreateView):
    model = Articles
    fields = ['title', 'content', 'picture', 'is_publicated']
    template_name = 'blog_new.html'
    success_url = reverse_lazy('articles_list')

class ArticlesListView(ListView):
    model = Articles
    template_name = 'blog.html'
    context_object_name = 'articles'
    def get_queryset(self):
        return Articles.objects.filter(is_publicated=True)

class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'blog_detail.html'
    context_object_name = 'article'
    def get_object(self, queryset=None):
        obj = super(ArticlesDetailView, self).get_object(queryset)
        obj.view_counter += 1
        obj.save(update_fields=['view_counter'])
        return obj

class ArticlesUpdateView(UpdateView):
    model = Articles
    fields = ['title', 'content', 'picture', 'is_publicated']
    template_name = 'blog_update_form.html'
    context_object_name = 'article'
    def get_success_url(self):
        return reverse_lazy('articles_detail', kwargs={'pk': self.object.pk})
    
class ArticlesDeleteView(DeleteView):
    model = Articles
    template_name = 'blog_confirm_delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('articles_list')