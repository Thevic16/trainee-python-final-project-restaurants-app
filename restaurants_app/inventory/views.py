from rest_framework.response import Response

from inventory.serializers import (UnitSerializer, IngredientSerializer,
                                   RecipeSerializer, InventorySerializer)
from inventory.models import Unit, Ingredient, Recipe, Inventory
from django.core.exceptions import ValidationError
from utilities.logger import Logger
from rest_framework import generics, mixins


# Views Unit
class UnitAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(UnitAPIView, self).get(request, *args, **kwargs)


class UnitAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Ingredient views
class IngredientAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(IngredientAPIView, self).get(request, *args, **kwargs)


class IngredientAPIDetailView(mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Recipe views
class RecipeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def get(self, request, *args, **kwargs):
        return super(RecipeAPIView, self).get(request, *args, **kwargs)


class RecipeAPIDetailView(mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.RetrieveAPIView):
    permission_classes = []
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
class InventoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def get(self, request, *args, **kwargs):
        return super(InventoryAPIView, self).get(request, *args, **kwargs)


class InventoryAPIDetailView(mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.RetrieveAPIView):
    permission_classes = []
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
