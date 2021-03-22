from django.contrib import admin
from .models import *


class ProductInCollectionInline(admin.TabularInline):
    model = ProductInCollection
    extra = 1


class CollectionAdmin(admin.ModelAdmin):
    inlines = [ProductInCollectionInline, ]


admin.site.register(Collection, CollectionAdmin)


