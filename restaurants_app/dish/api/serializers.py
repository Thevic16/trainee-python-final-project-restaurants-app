from rest_framework import serializers

from dish.models import MenuCategory, Dish


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

