from rest_framework import generics

from restaurant import models
from restaurant import serializers


class FoodType:
    queryset = models.FoodType.objects.all()
    serializer_class = serializers.FoodTypeSerializer


class FoodTypeList(FoodType, generics.ListCreateAPIView):
    pass


class FoodTypeDetail(FoodType, generics.RetrieveUpdateDestroyAPIView):
    pass


class PayType:
    queryset = models.PayType.objects.all()
    serializer_class = serializers.PayTypeSerializer


class PayTypeList(PayType, generics.ListCreateAPIView):
    pass


class PayTypeDetail(PayType, generics.RetrieveUpdateDestroyAPIView):
    pass


class Restaurant:
    queryset = models.Restaurant.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.RestaurantSerializerGet
        return serializers.RestaurantSerializerPost


class RestaurantList(Restaurant, generics.ListCreateAPIView):
    pass


class PayDay:

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.PayDayGet
        return serializers.PayDayPost

    def get_queryset(self):
        queryset = models.PayDay.objects.all()
        return queryset.filter(restaurant__pay_type__name='monthly')


class PayDayList(PayDay, generics.ListCreateAPIView):
    pass


class PayDayDetail(PayDay, generics.RetrieveUpdateDestroyAPIView):
    pass
