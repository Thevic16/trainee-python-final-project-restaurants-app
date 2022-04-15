from rest_framework import mixins, generics

from dish.api.serializers import MenuCategorySerializer
from dish.models import MenuCategory


# MenuCategory views
class MenuCategoryAPIDetailView(mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.RetrieveAPIView):
    """
    MenuCategory endpoint to retrieve, update and destroy,
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
    MenuCategory endpoint to create and list,
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
