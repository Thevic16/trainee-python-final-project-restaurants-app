from rest_framework import serializers

from restaurant.models import FoodType, PayDay, PayType, Restaurant
from restaurant.validations import PayDayValidator, RestaurantValidator


class FoodTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodType
        fields = '__all__'


class PayTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayType
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantSerializerPost(RestaurantSerializer):

    def validate(self, attrs):
        RestaurantValidator.commission_monthly_method(
            commission=attrs.get('commission'),
            pay_type=attrs.get('pay_type').name
        )
        RestaurantValidator.commission_bte_0_100(
            commission=attrs.get('commission'))
        return super().validate(attrs)


class RestaurantSerializerGet(RestaurantSerializer):
    food_type = serializers.StringRelatedField()
    pay_type = serializers.StringRelatedField()


class PayDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PayDay
        fields = '__all__'


class PayDayPost(PayDaySerializer):

    def validate(self, attrs):
        PayDayValidator.pay_day_lt_15(attrs.get('day'))
        PayDayValidator.monthly_restaurant(
            attrs.get('restaurant').pay_type.name)
        return super().validate(attrs)


class PayDayGet(PayDaySerializer):
    restaurant = serializers.StringRelatedField()
