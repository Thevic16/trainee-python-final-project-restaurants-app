from django.urls import path
from user.views import (GoogleSocialAuthClientView,
                        GoogleSocialAuthRestaurantAdministratorView)

urlpatterns = [
    path('google/client/', GoogleSocialAuthClientView.as_view()),
    path('google/restaurant-administrator/',
         GoogleSocialAuthRestaurantAdministratorView.as_view()),
]
