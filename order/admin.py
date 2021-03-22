from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    readonly_fields = ('price_per_item', 'total_price', )
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price', )
    inlines = [ProductInOrderInline, ]


admin.site.register(Order, OrderAdmin)
