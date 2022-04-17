from django.urls import path

from dish.api.views import (MenuCategoryAPIView,
                            MenuCategoryAPIDetailView,
                            DishAPIDetailView,
                            DishAPIAPIView)

app_name = 'dish'

urlpatterns = [
    # Paths MenuCategory
    path('menus_categories/', MenuCategoryAPIView.as_view()),
    path('menus_categories/<int:pk>/', MenuCategoryAPIDetailView.as_view(),
         name='menu-category-detail'),

    # Paths Dish
    path('dishes/',
         DishAPIDetailView.as_view({'get': 'list', 'post': 'create'})),
    path('dishes/<int:pk>/', DishAPIAPIView.as_view({'get': 'retrieve',
                                                     'put': 'update',
                                                     'patch': 'update',
                                                     'delete': 'destroy'}),
         name='dish-detail'),

]
