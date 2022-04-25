from rest_framework import serializers

from dish.models import MenuCategory, Dish, Promotion
from django.db import models
from rest_framework.reverse import reverse as api_reverse


# MenuCategory Serializer
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = [
            'id',
            'name',
            'restaurant',
        ]


# Dish Serializer
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = [
            'id',
            'name',
            'price',
            'description',
            'photo',
            'restaurant',
            'menu_category',
        ]

    def get_uri(self, obj: models.Model, model_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'dish:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['menu_category'] = instance.menu_category.name

        return response


# Promotion Serializer
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = [
            'id',
            'name',
            'price',
            'since_date',
            'up_to',
            'dishes',
            'branches',
            'restaurant',
        ]

    def get_uri(self, obj: models.Model, model_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'dish:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['dishes'] = []

        for dish in instance.dishes.all():
            response['dishes'].append(self.get_uri(dish, 'dish'))

        return response
