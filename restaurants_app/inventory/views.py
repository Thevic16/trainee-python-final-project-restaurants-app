from rest_framework.response import Response

from inventory.serializers import (UnitSerializer, IngredientSerializer,
                                   RecipeSerializer, InventorySerializer)
from inventory.models import Unit, Ingredient, Recipe, Inventory
from django.core.exceptions import ValidationError

from person.permissions import ReadOnly, IsRestaurantAdministrator, \
    IsBranchManager
from utilities.logger import Logger
from rest_framework import generics, mixins


# Views Unit
class UnitList(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [IsRestaurantAdministrator]
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(UnitList, self).get(request, *args, **kwargs)


class UnitDetail(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                 generics.RetrieveAPIView):
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Ingredient views
class IngredientList(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [IsRestaurantAdministrator]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(IngredientList, self).get(request, *args, **kwargs)


class IngredientDetail(mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.RetrieveAPIView):
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Recipe views
class RecipeList(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [IsRestaurantAdministrator]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def get(self, request, *args, **kwargs):
        return super(RecipeList, self).get(request, *args, **kwargs)


class RecipeDetail(mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.RetrieveAPIView):
    permission_classes = [IsRestaurantAdministrator]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def patch(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)


# Inventory views
class InventoryList(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [IsBranchManager]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def get(self, request, *args, **kwargs):
        return super(InventoryList, self).get(request, *args, **kwargs)


class InventoryDetail(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.RetrieveAPIView):
    permission_classes = [IsBranchManager]
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def patch(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)
