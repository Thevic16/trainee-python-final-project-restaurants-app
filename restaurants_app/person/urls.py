from django.urls import path
from person.views import (GoogleSocialAuthClientView,
                          GoogleSocialAuthRestaurantAdministratorView,
                          GoogleSocialAuthEmployeeView,
                          GoogleSocialAuthBranchManagerView)

urlpatterns = [
    path('google/clients/', GoogleSocialAuthClientView.as_view()),
    path('google/restaurant-administrators/',
         GoogleSocialAuthRestaurantAdministratorView.as_view()),
    path('google/employees/',
         GoogleSocialAuthEmployeeView.as_view()),
    path('google/branch-managers/',
         GoogleSocialAuthBranchManagerView.as_view()),
]
