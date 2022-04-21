from django.urls import path

from inventory.views import (UnitList, UnitDetail,
                             IngredientDetail, IngredientList,
                             RecipeList,
                             RecipeDetail, InventoryDetail,
                             InventoryList)

app_name = 'inventory'

urlpatterns = [
    # Paths Unit
    path('units/',
         UnitList.as_view()),
    path('units/<int:pk>/', UnitDetail.as_view(),
         name='unit-detail'),

    # Paths Ingredient
    path('ingredients/',
         IngredientList.as_view()),
    path('ingredients/<int:pk>/', IngredientDetail.as_view(),
         name='ingredient-detail'),

    # Paths Recipe
    path('recipes/',
         RecipeList.as_view()),
    path('recipes/<int:pk>/',
         RecipeDetail.as_view(),
         name='recipe-detail'),

    # Paths Inventory
    path('inventories/',
         InventoryList.as_view()),
    path('inventories/<int:pk>/',
         InventoryDetail.as_view(),
         name='inventory-detail'),
]
