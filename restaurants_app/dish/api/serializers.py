from rest_framework import serializers

from dish.models import MenuCategory, Dish, Promotion


# MenuCategory Serializer
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = [
            'id',
            'name',
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
            'menu_category',
        ]


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
        ]
