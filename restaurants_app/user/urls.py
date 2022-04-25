from django.urls import path
from user.views import (GoogleSocialAuthClientView,
                        GoogleSocialAuthRestaurantAdministratorView,
                        GoogleSocialAuthEmployeeView,
                        GoogleSocialAuthBranchManagerView)

urlpatterns = [
    path('google/client/', GoogleSocialAuthClientView.as_view()),
    path('google/restaurant-administrator/',
         GoogleSocialAuthRestaurantAdministratorView.as_view()),
    path('google/employee/',
         GoogleSocialAuthEmployeeView.as_view()),
    path('google/branch-manager/',
         GoogleSocialAuthBranchManagerView.as_view()),
]
