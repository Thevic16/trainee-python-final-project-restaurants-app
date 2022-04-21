from django.urls import path

from dish.views import (MenuCategoryAPIView,
                        MenuCategoryAPIDetailView,
                        DishAPIDetailView,
                        PromotionAPIDetailView,
                        DishAPIView, PromotionAPIView)

app_name = 'dish'

urlpatterns = [
    # Paths MenuCategory
    path('menus_categories/',
         MenuCategoryAPIView.as_view()),
    path('menus_categories/<int:pk>/', MenuCategoryAPIDetailView.as_view(),
         name='menu-category-detail'),

    # Paths Dish
    path('dishes/',
         DishAPIView.as_view()),
    path('dishes/<int:pk>/', DishAPIDetailView.as_view(),
         name='dish-detail'),

    # Paths Promotion
    path('promotions/',
         PromotionAPIView.as_view()),
    path('promotions/<int:pk>/',
         PromotionAPIDetailView.as_view(),
         name='promotions-detail'),
]
