from django.urls import path
from user.views import GoogleSocialAuthClientView

urlpatterns = [
    path('google/client/', GoogleSocialAuthClientView.as_view()),
]
