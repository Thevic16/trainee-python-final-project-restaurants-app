from django.urls import path

from dish.api.views import (MenuCategoryAPIView,
                            MenuCategoryAPIDetailView)

app_name = 'dish'

urlpatterns = [
    # Paths MenuCategory
    path('menus_categories/', MenuCategoryAPIView.as_view()),
    path('menus_categories/<int:pk>/', MenuCategoryAPIDetailView.as_view(),
         name='category-detail'),

]
