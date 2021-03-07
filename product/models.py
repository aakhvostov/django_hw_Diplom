from django.db import models
from django.conf import settings


class Product(models.Model):
    """ Товары """
    name = models.CharField(max_length=256, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'


class ProductImage(models.Model):
    """ Фото товара """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photo', verbose_name='Товар')
    image = models.ImageField(upload_to='media/productimage/', verbose_name='Фото товара')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return f'Фото {self. product}'


class Review(models.Model):
    """ Отзывы """
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES = (
        (ONE, 'Одна звезда'),
        (TWO, 'Две звезды'),
        (THREE, 'Три звезды'),
        (FOUR, 'Четыре звезды'),
        (FIVE, 'Пять звезд'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор отзыва')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='Товар')
    text = models.TextField(verbose_name='Отзыв')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=FIVE, verbose_name='Рейтинг товара')
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-author']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.id}: {self.author}/{self.product} - {self.rating}'


