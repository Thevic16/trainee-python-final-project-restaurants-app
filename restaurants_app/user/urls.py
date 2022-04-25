from django.urls import path
from user.views import (GoogleSocialAuthClientView,
                        GoogleSocialAuthRestaurantAdministratorView,
                        GoogleSocialAuthEmployeeView)

urlpatterns = [
    path('google/client/', GoogleSocialAuthClientView.as_view()),
    path('google/restaurant-administrator/',
         GoogleSocialAuthRestaurantAdministratorView.as_view()),
    path('google/employee/',
         GoogleSocialAuthEmployeeView.as_view()),
]
