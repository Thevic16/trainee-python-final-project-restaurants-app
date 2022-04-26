from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from restaurant import models
from restaurant import serializers
from restaurant.services import PayServices


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


class PayMonthly(viewsets.ModelViewSet):
    serializer_class = serializers.PaySerializer
    queryset = models.Pay.objects.all()

    @action(detail=True, methods=['post'])
    def pay_monthly(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        PayServices.monthtly_pay(
            restaurant_id=serializer.data.get('restaurant'),
            month_payed=serializer.data.get('month_payed')
        )
        return Response(serializer.data, status=201)

    @action(detail=True, methods=['get'])
    def payments(self, request):
        serializer = serializers.PayGetSerializer(self.queryset, many=True)
        return Response(serializer.data, status=200)


class BranchListView(generics.ListCreateAPIView):
    queryset = models.Branch.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.BranchGetSerializer
        return serializers.BranchPostSerializer
