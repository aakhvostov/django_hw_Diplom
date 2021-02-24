from rest_framework import serializers
from .models import *


class OrderSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ProductInOrderSerialiser(serializers.ModelSerializer):

    class Meta:
        model = ProductInOrder
        fields = '__all__'
