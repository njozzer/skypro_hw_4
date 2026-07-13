from django.urls import path

from blog import views

urlpatterns = [
    path('/', views.ArticlesListView.as_view(), name='articles_list'),
    path('/<int:pk>/', views.ArticlesDetailView.as_view(), name='articles_detail'),
    path('/new/', views.ArticlesCreateView.as_view(), name='articles_create'),
    path('/<int:pk>/edit/', views.ArticlesUpdateView.as_view(), name='articles_edit'),
    path('/<int:pk>/delete/', views.ArticlesDeleteView.as_view(), name='articles_delete'),
]