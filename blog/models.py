from django.db import models


# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    name = models.CharField(max_length=200, verbose_name='Категория')

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Пост'

    title = models.CharField(max_length=100, verbose_name='Нзавание')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзыв'

    author = models.CharField(max_length=100, verbose_name='Автор')
    text = models.TextField(verbose_name='Отзыв')
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.author