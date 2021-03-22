from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from product.models import Product


class Order(models.Model):
    """ Заказ """
    ORDER_STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('IN_PROGRESS', 'IN_PROGRESS'),
        ('DONE', 'DONE'),

    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    status = models.CharField(max_length=12, verbose_name='Статус', choices=ORDER_STATUS_CHOICES, default='NEW')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Итоговая цена', default=0)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id}. Владелец - {self.owner}. Сумма - {self.total_price}'


class ProductInOrder(models.Model):
    """ Товар в заказе """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар в заказе')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')
    price_per_item = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена товара')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Общая сумма')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.quantity * self.price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.order} - {self.product}'


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)
    order_total_price = 0
    for product in all_products_in_order:
        order_total_price += product.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
