from django.urls import path

from dish.api.views import (MenuCategoryAPIView,
                            MenuCategoryAPIDetailView,
                            DishAPIDetailView,
                            PromotionAPIDetailView,
                            DishAPIView, PromotionAPIView)

app_name = 'dish'

urlpatterns = [
    # Paths MenuCategory
    path('menus_categories/',
         MenuCategoryAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('menus_categories/<int:pk>/', MenuCategoryAPIDetailView.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'update',
         'delete': 'destroy'}),
         name='menu-category-detail'),

    # Paths Dish
    path('dishes/',
         DishAPIDetailView.as_view({'get': 'list', 'post': 'create'})),
    path('dishes/<int:pk>/', DishAPIView.as_view({'get': 'retrieve',
                                                     'put': 'update',
                                                     'patch': 'update',
                                                     'delete': 'destroy'}),
         name='dish-detail'),

    # Paths Promotion
    path('promotions/',
         PromotionAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('promotions/<int:pk>/',
         PromotionAPIDetailView.as_view({'get': 'retrieve',
                                      'put': 'update',
                                      'patch': 'update',
                                      'delete': 'destroy'}),
         name='promotion-detail'),

]
