from django.urls import path

from order import views


urlpatterns = [
    path('status/', views.StatusView.as_view()),
    path('item-types/', views.ItemTypeView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('item-order/', views.ItemOrderView.as_view()),
    path('send-order/<int:pk>', views.SendOrder.as_view()),
    # Paths Menu
    path('menus/<int:pk>/', views.MenuDetail.as_view({'get': 'retrieve'}),
         name='menu-detail'),
]
