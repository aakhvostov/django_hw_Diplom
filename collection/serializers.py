from rest_framework import serializers
from .models import Collection, ProductInCollection
from product.serializers import ProductShortSerialiser


class ProductInCollectionSerialiser(serializers.ModelSerializer):

    product = ProductShortSerialiser(read_only=True)

    class Meta:
        model = ProductInCollection
        fields = ("product",)


class CollectionSerialiser(serializers.ModelSerializer):

    collect_products = ProductInCollectionSerialiser(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'title', 'text', 'collect_products', 'created_at', 'updated_at')

