from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from dish.api.serializers import (MenuCategorySerializer, DishSerializer,
                                  PromotionSerializer)
from dish.models import MenuCategory, Dish, Promotion

from restaurant.models import Restaurant, Branch
from utilities.logger import Logger


# MenuCategory views
class MenuCategoryAPIView(GenericViewSet):
    """
    MenuCategory view set to create and list,only restaurant administrator role is
     allowed to perform these actions.
    """
    permission_classes = []
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # After create person model and implement jwt this has to be modified.
        object = MenuCategory(name=serializer.data['name'],
                              restaurant=Restaurant.objects.all().first())

        object.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class MenuCategoryAPIDetailView(GenericViewSet):
    """
    MenuCategory view set to retrieve, update, partial_update and destroy, only
     restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

    def retrieve(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def update(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object.name = serializer.data['name']
        object.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object.name = serializer.data['name']
        object.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def destroy(self, request, pk):
        object = self.get_object()
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Dish views
class DishAPIView(GenericViewSet):
    """
    Dish view set to create and list,only restaurant administrator role is
     allowed to perform these actions.
    """
    permission_classes = []
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # After create person model and implement jwt this has to be modified.
        object = Dish(name=serializer.data['name'],
                      price=serializer.data['price'],
                      description=serializer.data['description'],
                      photo=serializer.data['photo'],
                      restaurant=Restaurant.objects.all().first(),
                      menu_category=MenuCategory.objects.get(
                          id=serializer.data['menu_category']))

        object.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class DishAPIDetailView(GenericViewSet):
    """
    Dish view set to retrieve, update, partial_update and destroy, only
     restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def retrieve(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def update(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object.name = serializer.data['name']
        object.price = serializer.data['price']
        object.description = serializer.data['description']
        object.photo = serializer.data['photo']
        object.menu_category = MenuCategory.objects.get(
            id=serializer.data['menu_category'])

        object.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object.name = serializer.data['name']
        object.price = serializer.data['price']
        object.description = serializer.data['description']
        object.photo = serializer.data['photo']
        object.menu_category = MenuCategory.objects.get(
            id=serializer.data['menu_category'])

        object.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def destroy(self, request, pk):
        object = self.get_object()
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Promotion views
class PromotionAPIDetailView(GenericViewSet):
    """
    Promotion view set to create and list,only restaurant administrator role is
     allowed to perform these actions.
    """
    permission_classes = []
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # After create person model and implement jwt this has to be
        # modified.
        object = Promotion(name=serializer.data['name'],
                           price=serializer.data['price'],
                           since_date=serializer.data['since_date'],
                           up_to=serializer.data['up_to'])

        # Here It is necessary to save before using the many-to-many
        # relationships
        try:
            object.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Assigning many-to-many relationships
        for dish in Dish.objects.filter(pk__in=serializer.data['dishes']):
            object.dishes.add(dish)

        for branch in Branch.objects.filter(
                pk__in=serializer.data['branches']):
            object.branches.add(branch)

        object.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class PromotionAPIView(GenericViewSet):
    """
    Promotion view set to retrieve, update, partial_update and destroy,only
     restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def retrieve(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def update(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object.name = serializer.data['name']
        object.price = serializer.data['price']
        object.since_date = serializer.data['since_date']
        object.up_to = serializer.data['up_to']

        for dish in Dish.objects.filter(pk__in=serializer.data['dishes']):
            object.dishes.add(dish)

        for branch in Branch.objects.filter(
                pk__in=serializer.data['branches']):
            object.branches.add(branch)

        try:
            object.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object.name = serializer.data['name']
        object.price = serializer.data['price']
        object.since_date = serializer.data['since_date']
        object.up_to = serializer.data['up_to']

        for dish in Dish.objects.filter(pk__in=serializer.data['dishes']):
            object.dishes.add(dish)

        for branch in Branch.objects.filter(
                pk__in=serializer.data['branches']):
            object.branches.add(branch)

        try:
            object.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(object)
        return Response(serializer.data)

    def destroy(self, request, pk):
        object = self.get_object()
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
