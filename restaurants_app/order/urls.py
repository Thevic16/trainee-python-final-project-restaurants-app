from django.urls import path

from order import views


urlpatterns = [
    path('status/', views.StatusView.as_view()),
    path('item-types/', views.ItemTypeView.as_view()),
]
