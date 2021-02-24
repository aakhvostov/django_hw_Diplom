from rest_framework import serializers
from .models import *


class CollectionSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'


class ProductInCollectionSerialiser(serializers.ModelSerializer):

    class Meta:
        model = ProductInCollection
        fields = '__all__'
