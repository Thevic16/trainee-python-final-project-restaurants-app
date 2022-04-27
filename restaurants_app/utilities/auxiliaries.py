import os

from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
import datetime


def get_uri(request, pk: int, model_name: str, app_name: str):
    return api_reverse(f'{app_name}:{model_name}-detail',
                       kwargs={'pk': pk}, request=request)


expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.email,
        'expires': timezone.now() + expire_delta - datetime.timedelta(
            seconds=int(os.environ.get('EXPIRES_TIME_SECONDS')))
    }
