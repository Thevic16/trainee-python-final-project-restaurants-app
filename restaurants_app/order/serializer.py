from rest_framework import serializers

from order.models import ItemType, Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class ItemTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemType
        fields = '__all__'
