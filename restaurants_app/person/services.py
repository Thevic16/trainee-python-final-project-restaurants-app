import datetime
from rest_framework_jwt.settings import api_settings
from django.utils import timezone

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


class TokenServices:
    @staticmethod
    def get_token(person: "Person"):  # instance of the model
        payload = jwt_payload_handler(person)
        token = jwt_encode_handler(payload)
        return token

    @staticmethod
    def get_expires():
        return timezone.now() + expire_delta - datetime.timedelta(
            seconds=7200)
