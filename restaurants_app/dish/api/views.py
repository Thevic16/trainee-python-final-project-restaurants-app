from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from dish.api.serializers import (MenuCategorySerializer, DishSerializer)
from dish.models import MenuCategory, Dish

# MenuCategory views
from restaurant.models import Restaurant
from utilities.logger import Logger
from utilities.mixins import ReadWriteSerializerMixin


class MenuCategoryAPIDetailView(mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.RetrieveAPIView):
    """
    MenuCategory view to retrieve, update and destroy,
    Only restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    serializer_class = MenuCategorySerializer
    queryset = MenuCategory.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MenuCategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    MenuCategory view to create and list,
    Only restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    ordering_fields = ('id', 'name')
    search_fields = ('id', 'name')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MenuCategoryAPIView, self).get(request, *args, **kwargs)


# Dish views
class DishAPIDetailView(GenericViewSet):
    """
    Dish view set to create, list, retrieve and destroy
    Only restaurant administrator role is allowed to perform these actions.
    """
    permission_classes = []
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object = Dish(name=serializer.data['name'],
                      price=serializer.data['price'],
                      description=serializer.data['description'],
                      photo=serializer.data['photo'],
                      restaurant=Restaurant.objects.all().first(),
                      menu_category=MenuCategory.objects.get(
                          id=serializer.data['menu_category']))

        object.save()

        # serializer.save(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class DishAPIAPIView(GenericViewSet):
    """
    Dish view set to create, list, retrieve and destroy
    Only restaurant administrator role is allowed to perform these actions.
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

        return Response(serializer.data)

    def destroy(self, request, pk):
        object = self.get_object()
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
