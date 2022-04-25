from rest_framework.viewsets import ViewSet
from order.map import MapServices
from rest_framework.response import Response


# Create your views here.
class MenuDetail(ViewSet):
    def retrieve(self, request, pk=None):
        MapServices.request = request
        return Response(MapServices.get_menu_map_dict_by_branch(pk))
