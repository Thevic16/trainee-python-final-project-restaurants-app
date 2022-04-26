from django.urls import path
from person.views import (SocialAuthClientView,
                          SocialAuthRestaurantAdministratorView,
                          SocialAuthEmployeeView,
                          SocialAuthBranchManagerView,
                          SocialAuthPortalManagerView,
                          SocialAuthView)

urlpatterns = [
    path('persons/auth/', SocialAuthView.as_view()),
    path('persons/clients/', SocialAuthClientView.as_view()),
    path('persons/restaurant-administrators/',
         SocialAuthRestaurantAdministratorView.as_view()),
    path('persons/employees/',
         SocialAuthEmployeeView.as_view()),
    path('persons/branch-managers/',
         SocialAuthBranchManagerView.as_view()),
    path('persons/portal-managers/',
         SocialAuthPortalManagerView.as_view()),
]
