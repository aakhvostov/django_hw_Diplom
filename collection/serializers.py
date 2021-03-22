from rest_framework import serializers
from .models import Collection, ProductInCollection
from product.serializers import ProductShortSerialiser


class ProductInCollectionSerialiser(serializers.ModelSerializer):

    class Meta:
        model = ProductInCollection
        fields = '__all__'


class CollectionSerialiser(serializers.ModelSerializer):

    products = ProductShortSerialiser(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'title', 'text', 'products', 'created_at', 'updated_at')
    #  ДОДЕЛАТЬ! вывод на показ всех продуктов в подборке!

