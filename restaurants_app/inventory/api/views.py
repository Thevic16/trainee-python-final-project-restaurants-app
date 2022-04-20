from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from dish.models import Dish
from inventory.api.serializers import UnitSerializer, IngredientSerializer, \
    RecipeSerializer, InventorySerializer
from inventory.models import Unit, Ingredient, Recipe, Inventory
from django.core.exceptions import ValidationError
from utilities.logger import Logger

# Unit views
from restaurant.models import Branch


class UnitAPIView(GenericViewSet):
    """
    Unit view set to create and list,only restaurant administrator role is
     allowed to perform these actions.
    """
    permission_classes = []
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        unit = Unit(name=serializer.data['name'],
                    abbreviation=serializer.data['abbreviation'])

        unit.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(unit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class UnitAPIDetailView(GenericViewSet):
    """
    Unit view set to retrieve, update, partial_update and destroy, only
     restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def retrieve(self, request, pk):
        unit = self.get_object()
        serializer = self.get_serializer(unit)
        return Response(serializer.data)

    def update(self, request, pk):
        unit = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        unit.name = serializer.data['name']
        unit.abbreviation = serializer.data['abbreviation']
        unit.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(unit)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        unit = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        unit.name = serializer.data['name']
        unit.abbreviation = serializer.data['abbreviation']
        unit.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(unit)
        return Response(serializer.data)

    def destroy(self, request, pk):
        unit = self.get_object()
        unit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Ingredient views
class IngredientAPIView(GenericViewSet):
    """
    Ingredient view set to create and list,only restaurant administrator role
     is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ingredient = Ingredient(name=serializer.data['name'],
                                unit=Unit.objects.get(
                                    id=serializer.data['unit']))

        ingredient.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(ingredient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class IngredientAPIDetailView(GenericViewSet):
    """
    Ingredient view set to retrieve, update, partial_update and destroy, only
     restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def retrieve(self, request, pk):
        ingredient = self.get_object()
        serializer = self.get_serializer(ingredient)
        return Response(serializer.data)

    def update(self, request, pk):
        ingredient = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ingredient.name = serializer.data['name']
        ingredient.unit = Unit.objects.get(id=serializer.data['unit'])
        ingredient.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(ingredient)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        ingredient = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ingredient.name = serializer.data['name']
        ingredient.unit = Unit.objects.get(id=serializer.data['unit'])
        ingredient.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(ingredient)
        return Response(serializer.data)

    def destroy(self, request, pk):
        ingredient = self.get_object()
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Recipe views
class RecipeAPIView(GenericViewSet):
    """
    Recipe view set to create and list,only restaurant administrator role
     is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recipe = Recipe(ingredient=Ingredient.objects.get(
            id=serializer.data['ingredient']),
            quantity=serializer.data['quantity'],
            dish=Dish.objects.get(
                id=serializer.data['dish'])
        )

        try:
            recipe.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class RecipeAPIDetailView(GenericViewSet):
    """
    Recipe view set to retrieve, update, partial_update and destroy, only
     restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def retrieve(self, request, pk):
        recipe = self.get_object()
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)

    def update(self, request, pk):
        recipe = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recipe.ingredient = Ingredient.objects.get(
            id=serializer.data['ingredient'])
        recipe.quantity = serializer.data['quantity']
        recipe.dish = Dish.objects.get(
            id=serializer.data['dish'])

        try:
            recipe.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        recipe = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recipe.ingredient = Ingredient.objects.get(
            id=serializer.data['ingredient'])
        recipe.quantity = serializer.data['quantity']
        recipe.dish = Dish.objects.get(
            id=serializer.data['dish'])

        try:
            recipe.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)

    def destroy(self, request, pk):
        recipe = self.get_object()
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Inventory views
class InventoryAPIView(GenericViewSet):
    """
    Inventory view set to create and list,only branch manager role
     is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        inventory = Inventory(ingredient=Ingredient.objects.get(
            id=serializer.data['ingredient']),
            availability=serializer.data['availability'],
            branch=Branch.objects.get(
                id=serializer.data['branch'])
        )

        try:
            inventory.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(inventory)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class InventoryAPIDetailView(GenericViewSet):
    """
    Inventory view set to retrieve, update, partial_update and destroy, only
     branch manager role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def retrieve(self, request, pk):
        inventory = self.get_object()
        serializer = self.get_serializer(inventory)
        return Response(serializer.data)

    def update(self, request, pk):
        inventory = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        inventory.ingredient = Ingredient.objects.get(
            id=serializer.data['ingredient'])
        inventory.availability = serializer.data['availability']
        inventory.branch = Branch.objects.get(
            id=serializer.data['branch'])

        try:
            inventory.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(inventory)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        inventory = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        inventory.ingredient = Ingredient.objects.get(
            id=serializer.data['ingredient'])
        inventory.availability = serializer.data['availability']
        inventory.branch = Branch.objects.get(
            id=serializer.data['branch'])

        try:
            inventory.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(inventory)
        return Response(serializer.data)

    def destroy(self, request, pk):
        inventory = self.get_object()
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
