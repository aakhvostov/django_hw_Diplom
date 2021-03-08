from rest_framework import serializers
from .models import Collection, ProductInCollection


class ProductInCollectionSerialiser(serializers.ModelSerializer):

    class Meta:
        model = ProductInCollection
        fields = '__all__'


class CollectionSerialiser(serializers.ModelSerializer):

    # products = ProductInCollectionSerialiser(read_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'title', 'text', 'created_at', 'updated_at')
        # fields = ('id', 'title', 'text', 'products', 'created_at', 'updated_at')

