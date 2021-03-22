from django.db import models
from product.models import Product


class Collection(models.Model):
    """ Подборка """
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст подборки')
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-title']
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return f'{self.id}: {self.title}'


class ProductInCollection(models.Model):
    """ Товар в подборке """
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='collect_products',
                                   verbose_name='Подборка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="collect_products",
                                verbose_name='Товар в подборке', )

    class Meta:
        verbose_name = 'Товар в подборке'
        verbose_name_plural = 'Товары в подборке'