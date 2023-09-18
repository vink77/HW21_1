from django.db import models
from datetime import datetime

from django.utils.text import slugify


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='slug')
    conteхt = models.TextField(verbose_name='Содержимое')
    preview_img = models.ImageField(upload_to='blog/images/', verbose_name='Превью(изображение)')
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y")
    date_create = models.DateField(verbose_name='Дата создания', default=current_time)
    sign_of_publication = models.BooleanField(verbose_name='Признак публикации', default=True)
    view_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}'


class Meta:
    verbose_name = 'блог'
    verbose_name_plural = 'блога'
    ordering = ('title',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)