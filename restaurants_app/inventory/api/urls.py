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
         UnitAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('units/<int:pk>/', UnitAPIDetailView.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'update',
         'delete': 'destroy'}),
         name='unit-detail'),

    # Paths Ingredient
    path('ingredients/',
         IngredientAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('ingredients/<int:pk>/', IngredientAPIDetailView.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'update',
         'delete': 'destroy'}),
         name='ingredient-detail'),

    # Paths Recipe
    path('recipes/',
         RecipeAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('recipes/<int:pk>/',
         RecipeAPIDetailView.as_view({'get': 'retrieve',
                                      'put': 'update',
                                      'patch': 'update',
                                      'delete': 'destroy'}),
         name='recipe-detail'),

    # Paths Inventory
    path('inventories/',
         InventoryAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('inventories/<int:pk>/',
         InventoryAPIDetailView.as_view({'get': 'retrieve',
                                         'put': 'update',
                                         'patch': 'update',
                                         'delete': 'destroy'}),
         name='inventory-detail'),
]
