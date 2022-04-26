from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from order import serializer
from order import services
from order.map import MapServices
from order.models import ItemOrder, ItemType, Order, Status
from order.validations import OrderValidator


class StatusView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = serializer.StatusSerializer


class ItemTypeView(generics.ListCreateAPIView):
    queryset = ItemType.objects.all()
    serializer_class = serializer.ItemTypeSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializer.OrderSerializerGet
        return serializer.OrderSerializerPost


class SendOrder(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializerUpdate

    def perform_update(self, serializer):
        order = self.get_object()
        OrderValidator.order_preparing(order)
        services.OrderServices().update_ingredients(order.id, order.branch_id)
        return super().perform_update(serializer)


class ItemOrderView(generics.ListCreateAPIView):
    queryset = ItemOrder.objects.all()
    serializer_class = serializer.ItemOrderSerializer


# Create your views here.
class MenuDetail(ViewSet):
    """
    An endpoint that allows retrieving the menu information for a specific
     branch with the HTTP method get, based on the id of the branch.
     Everybody has permission to access this resource.
    """
    def retrieve(self, request, pk=None):
        MapServices.request = request
        return Response(MapServices.get_menu_map_dict_by_branch(pk))
