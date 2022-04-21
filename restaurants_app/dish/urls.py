from django.urls import path

from dish.views import (MenuCategoryList,
                        MenuCategoryDetail,
                        DishDetail,
                        PromotionDetail,
                        DishList, PromotionList)

app_name = 'dish'

urlpatterns = [
    # Paths MenuCategory
    path('menus-categories/',
         MenuCategoryList.as_view()),
    path('menus-categories/<int:pk>/', MenuCategoryDetail.as_view(),
         name='menu-category-detail'),

    # Paths Dish
    path('dishes/',
         DishList.as_view()),
    path('dishes/<int:pk>/', DishDetail.as_view(),
         name='dish-detail'),

    # Paths Promotion
    path('promotions/',
         PromotionList.as_view()),
    path('promotions/<int:pk>/',
         PromotionDetail.as_view(),
         name='promotions-detail'),
]
