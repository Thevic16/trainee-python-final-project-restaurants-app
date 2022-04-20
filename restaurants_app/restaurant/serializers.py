from rest_framework import serializers

from restaurant.models import FoodType, Pay, PayDay, PayType, Restaurant
from restaurant.validations import (
    PayDayValidator, PayValidator, RestaurantValidator)


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


class PaySerializer(serializers.ModelSerializer):
    pay = serializers.ReadOnlyField()
    pay_type = serializers.ReadOnlyField()

    class Meta:
        model = Pay
        fields = '__all__'

    def validate(self, attrs):
        PayValidator.valid_month(attrs.get('month_payed'))
        PayDayValidator.monthly_restaurant(
            attrs.get('restaurant').pay_type.name)
        return super().validate(attrs)


class PayGetSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()
    pay_type = serializers.StringRelatedField()

    class Meta:
        model = Pay
        fields = '__all__'
