from django.urls import path

from order.views import MenuDetail

app_name = 'order'

urlpatterns = [
    # Paths Menu
    path('menus/<int:pk>/', MenuDetail.as_view({'get': 'retrieve'}),
         name='menu-detail'),
]
