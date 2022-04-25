from rest_framework import serializers

from order.models import ItemOrder, ItemType, Order, Status
from order.validations import ItemOrderValidator


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class ItemTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemType
        fields = '__all__'


class OrderSerializerGet(serializers.ModelSerializer):
    delivery_type = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('branch', 'delivery_type', 'direction', 'client')


class OrderSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('status',)


class ItemOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemOrder
        fields = '__all__'

    def validate(self, attrs):
        ItemOrderValidator.dish_or_promotion(
            dish=attrs.get('dish', None),
            promotion=attrs.get('promotion', None)
        )
        return super().validate(attrs)
