from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericUUIDTaggedItemBase
from pytils.translit import slugify
from unidecode import unidecode


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:select_category', args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique_for_date='created')
    category = models.ForeignKey(Category,
                                 related_name='posts',
                                 on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               related_name='posts',
                               on_delete=models.CASCADE)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])


class Comment(models.Model):
    author = models.ForeignKey(User,
                               related_name='comments',
                               on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['created'])]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author.username} - {self.post.title}'
