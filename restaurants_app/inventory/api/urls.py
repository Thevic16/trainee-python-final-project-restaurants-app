from django.urls import path

from inventory.api.views import (UnitAPIView, UnitAPIDetailView,
                                 IngredientAPIDetailView, IngredientAPIView,
                                 RecipeAPIView,
                                 RecipeAPIDetailView, InventoryAPIDetailView,
                                 InventoryAPIView)

app_name = 'inventory'

urlpatterns = [
    # Paths Unit
    path('units/',
         UnitAPIView.as_view()),
    path('units/<int:pk>/', UnitAPIDetailView.as_view(),
         name='unit-detail'),

    # Paths Ingredient
    path('ingredients/',
         IngredientAPIView.as_view()),
    path('ingredients/<int:pk>/', IngredientAPIDetailView.as_view(),
         name='ingredient-detail'),

    # Paths Recipe
    path('recipes/',
         RecipeAPIView.as_view()),
    path('recipes/<int:pk>/',
         RecipeAPIDetailView.as_view(),
         name='recipe-detail'),

    # Paths Inventory
    path('inventories/',
         InventoryAPIView.as_view()),
    path('inventories/<int:pk>/',
         InventoryAPIDetailView.as_view(),
         name='inventory-detail'),
]
