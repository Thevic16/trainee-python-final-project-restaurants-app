from django.urls import path

from user.views import GoogleSocialAuthView

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
]
