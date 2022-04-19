from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from dish.api.serializers import (MenuCategorySerializer, DishSerializer,
                                  PromotionSerializer, DishPhotoSerializer)
from dish.models import MenuCategory, Dish, Promotion, DishPhoto

from restaurant.models import Restaurant, Branch
from utilities.logger import Logger
from rest_framework import generics, mixins


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
        menu_category = MenuCategory(name=serializer.data['name'],
                                     restaurant=Restaurant.objects.all().first())

        menu_category.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(menu_category)
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
        menu_category = self.get_object()
        serializer = self.get_serializer(menu_category)
        return Response(serializer.data)

    def update(self, request, pk):
        menu_category = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        menu_category.name = serializer.data['name']
        menu_category.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(menu_category)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        menu_category = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        menu_category.name = serializer.data['name']
        menu_category.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(menu_category)
        return Response(serializer.data)

    def destroy(self, request, pk):
        menu_category = self.get_object()
        menu_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Dish views
class DishAPIView(GenericViewSet):
    """
    Dish view set to create and list,only restaurant administrator role is
     allowed to perform these actions.
    """
    permission_classes = []
    queryset = Dish.objects.all().filter(is_deleted=False)
    serializer_class = DishSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # After create person model and implement jwt this has to be modified.
        dish = Dish(name=serializer.data['name'],
                    price=serializer.data['price'],
                    description=serializer.data['description'],
                    restaurant=Restaurant.objects.all().first(),
                    menu_category=MenuCategory.objects.get(
                        id=serializer.data['menu_category']))

        dish.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(dish)
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
    queryset = Dish.objects.all().filter(is_deleted=False)
    serializer_class = DishSerializer

    def retrieve(self, request, pk):
        dish = self.get_object()
        serializer = self.get_serializer(dish)
        return Response(serializer.data)

    def update(self, request, pk):
        dish = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dish.name = serializer.data['name']
        dish.price = serializer.data['price']
        dish.description = serializer.data['description']
        dish.menu_category = MenuCategory.objects.get(
            id=serializer.data['menu_category'])

        dish.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(dish)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        dish = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dish.name = serializer.data['name']
        dish.price = serializer.data['price']
        dish.description = serializer.data['description']
        dish.menu_category = MenuCategory.objects.get(
            id=serializer.data['menu_category'])

        dish.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(dish)
        return Response(serializer.data)

    def destroy(self, request, pk):
        dish = self.get_object()
        dish.is_deleted = True
        dish.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


# DishPhoto
class DishPhotoAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = DishPhoto.objects.all()
    serializer_class = DishPhotoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DishPhotoAPIView, self).get(request, *args, **kwargs)


class DishPhotoAPIDetailView(mixins.DestroyModelMixin,
                             generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = DishPhotoSerializer
    queryset = DishPhoto.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Promotion views
class PromotionAPIView(GenericViewSet):
    """
    Promotion view set to create and list,only restaurant administrator role is
     allowed to perform these actions.
    """
    permission_classes = []
    queryset = Promotion.objects.all().filter(is_deleted=False)
    serializer_class = PromotionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # After create person model and implement jwt this has to be
        # modified.
        promotion = Promotion(name=serializer.data['name'],
                              price=serializer.data['price'],
                              since_date=serializer.data['since_date'],
                              up_to=serializer.data['up_to'])

        # Here It is necessary to save before using the many-to-many
        # relationships
        try:
            promotion.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Assigning many-to-many relationships
        for dish in Dish.objects.filter(pk__in=serializer.data['dishes']):
            promotion.dishes.add(dish)

        for branch in Branch.objects.filter(
                pk__in=serializer.data['branches']):
            promotion.branches.add(branch)

        promotion.save()

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(promotion)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class PromotionAPIDetailView(GenericViewSet):
    """
    Promotion view set to retrieve, update, partial_update and destroy,only
     restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Promotion.objects.all().filter(is_deleted=False)
    serializer_class = PromotionSerializer

    def retrieve(self, request, pk):
        promotion = self.get_object()
        serializer = self.get_serializer(promotion)
        return Response(serializer.data)

    def update(self, request, pk):
        promotion = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        promotion.name = serializer.data['name']
        promotion.price = serializer.data['price']
        promotion.since_date = serializer.data['since_date']
        promotion.up_to = serializer.data['up_to']

        for dish in Dish.objects.filter(pk__in=serializer.data['dishes']):
            promotion.dishes.add(dish)

        for branch in Branch.objects.filter(
                pk__in=serializer.data['branches']):
            promotion.branches.add(branch)

        try:
            promotion.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(promotion)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        promotion = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        promotion.name = serializer.data['name']
        promotion.price = serializer.data['price']
        promotion.since_date = serializer.data['since_date']
        promotion.up_to = serializer.data['up_to']

        for dish in Dish.objects.filter(pk__in=serializer.data['dishes']):
            promotion.dishes.add(dish)

        for branch in Branch.objects.filter(
                pk__in=serializer.data['branches']):
            promotion.branches.add(branch)

        try:
            promotion.save()
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

        # Overwriting the serializer to add id field.
        serializer = self.get_serializer(promotion)
        return Response(serializer.data)

    def destroy(self, request, pk):
        promotion = self.get_object()
        promotion.is_deleted = True
        promotion.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
