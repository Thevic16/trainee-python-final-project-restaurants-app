from google.auth.transport import requests
from google.oauth2 import id_token
import os


class Provider:
    """Provider class to fetch the person info and return it"""

    @staticmethod
    def validate(auth_token):
        """
        validate method Queries the Google oAUTH2 api to fetch the person info
        """
        try:
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request())

            if os.environ.get('SOCIAL_ISS') in idinfo['iss']:
                return idinfo

        except:
            return "The token is either invalid or has expired"
        