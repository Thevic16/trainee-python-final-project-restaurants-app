from django.urls import path

from dish.api.views import (MenuCategoryAPIView,
                            MenuCategoryAPIDetailView,
                            DishAPIDetailView,
                            PromotionAPIDetailView,
                            DishAPIView, PromotionAPIView, DishPhotoAPIView,
                            DishPhotoAPIDetailView)

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
         DishAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('dishes/<int:pk>/', DishAPIDetailView.as_view({'get': 'retrieve',
                                                        'put': 'update',
                                                        'patch': 'update',
                                                        'delete': 'destroy'}),
         name='dish-detail'),

    # Paths DishPhoto
    path('dishes_photos/',
         DishPhotoAPIView.as_view()),
    path('dishes_photos/<int:pk>/', DishPhotoAPIDetailView.as_view(),
         name='dish-detail'),

    # Paths Promotion
    path('promotions/',
         PromotionAPIView.as_view()),
    path('promotions/<int:pk>/',
         PromotionAPIDetailView.as_view({'get': 'retrieve',
                                         'put': 'update',
                                         'patch': 'update',
                                         'delete': 'destroy'}),
         name='dish-photo-detail'),
]
