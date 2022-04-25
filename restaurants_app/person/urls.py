from django.urls import path
from person.views import (GoogleSocialAuthClientView,
                          GoogleSocialAuthRestaurantAdministratorView,
                          GoogleSocialAuthEmployeeView,
                          GoogleSocialAuthBranchManagerView,
                          GoogleSocialAuthPortalManagerView,
                          GoogleSocialAuthView)

urlpatterns = [
    path('google/auth/', GoogleSocialAuthView.as_view()),
    path('google/create/clients/', GoogleSocialAuthClientView.as_view()),
    path('google/create/restaurant-administrators/',
         GoogleSocialAuthRestaurantAdministratorView.as_view()),
    path('google/create/employees/',
         GoogleSocialAuthEmployeeView.as_view()),
    path('google/create/branch-managers/',
         GoogleSocialAuthBranchManagerView.as_view()),
    path('google/create/portal-managers/',
         GoogleSocialAuthPortalManagerView.as_view()),
]
