from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= Item
        fields = ('id', 'name', 'price', 'details', 'photo_1_url', 'photo_2_url',)