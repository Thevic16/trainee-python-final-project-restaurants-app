from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response

from dish.api.serializers import (MenuCategorySerializer, DishSerializer,
                                  PromotionSerializer)
from dish.models import MenuCategory, Dish, Promotion
from utilities.logger import Logger
from rest_framework import generics, mixins


# MenuCategory views
class MenuCategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MenuCategoryAPIView, self).get(request, *args, **kwargs)


class MenuCategoryAPIDetailView(mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = MenuCategorySerializer
    queryset = MenuCategory.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Dish views
class DishAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = Dish.objects.all().filter(is_deleted=False)
    serializer_class = DishSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DishAPIView, self).get(request, *args, **kwargs)


class DishAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = DishSerializer
    queryset = Dish.objects.all().filter(is_deleted=False)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        dish = self.get_object()
        dish.is_deleted = True
        dish.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Promotion views
class PromotionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    queryset = Promotion.objects.all().filter(is_deleted=False)
    serializer_class = PromotionSerializer

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def get(self, request, *args, **kwargs):
        return super(PromotionAPIView, self).get(request, *args, **kwargs)


class PromotionAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                             generics.RetrieveAPIView):
    permission_classes = []
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all().filter(is_deleted=False)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        promotion = self.get_object()
        promotion.is_deleted = True
        promotion.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
