from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое')
    picture = models.ImageField(upload_to='articles/', verbose_name='превью', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_publicated = models.BooleanField(verbose_name='признак публикац', default=False)
    view_counter = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title