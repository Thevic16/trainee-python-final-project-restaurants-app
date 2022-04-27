from rest_framework import serializers

# Unit Serializer
from inventory.models import Unit, Ingredient, Recipe, Inventory
from django.db import models
from rest_framework.reverse import reverse as api_reverse


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = [
            'id',
            'name',
            'abbreviation',
        ]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'unit',
        ]

    def get_uri(self, obj: models.Model, model_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'inventory:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['unit'] = instance.unit.abbreviation

        return response


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id',
            'ingredient',
            'quantity',
            'dish',
        ]

    def get_uri(self, obj: models.Model, model_name: str, app_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'{app_name}:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['ingredient'] = self.get_uri(instance.ingredient,
                                              'ingredient', 'inventory')
        response['dish'] = self.get_uri(instance.dish, 'dish', 'dish')

        return response


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'ingredient',
            'availability',
            'branch',
        ]

    def get_uri(self, obj: models.Model, model_name: str, app_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'{app_name}:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['ingredient'] = self.get_uri(instance.ingredient,
                                              'ingredient', 'inventory')

        return response
