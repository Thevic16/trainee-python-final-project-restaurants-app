from rest_framework import generics

from order.models import ItemType, Status
from order.serializer import ItemTypeSerializer, StatusSerializer


class StatusView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ItemTypeView(generics.ListCreateAPIView):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer
