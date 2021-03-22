from rest_framework import serializers
from product.serializers import ProductShortSerialiser, UserSerializer
from .models import Order, ProductInOrder


class ProductInOrderSerialiser(serializers.ModelSerializer):
    product = ProductShortSerialiser()

    class Meta:
        model = ProductInOrder
        fields = '__all__'


class OrderSerialiser(serializers.ModelSerializer):
    products = ProductInOrderSerialiser(many=True, read_only=True)
    owner = UserSerializer()

    class Meta:
        model = Order
        fields = ('id', 'owner', 'status', 'products', 'total_price', 'created_at', 'updated_at')
