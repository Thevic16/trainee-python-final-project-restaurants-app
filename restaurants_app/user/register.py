from user.models import User
import os
import random
from rest_framework.exceptions import AuthenticationFailed

from utilities.logger import Logger


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def authenticate(email: str, password: str):
    user = User.objects.filter(email=email).first()

    if user:
        return user
    else:
        raise AuthenticationFailed


def register_social_user(provider: str, user_id: int, email: str, name: str,
                         user_role: str, restaurant_id: int):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            Logger.debug(f'registered_user: {registered_user}')

            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'tokens': registered_user.tokens()}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' +
                       filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': os.environ.get('SOCIAL_SECRET')}

        if user_role == 'Client':
            user = User.objects.create_client_user(**user)
        if user_role == 'Restaurant Administrator':
            user = User.objects.create_restaurant_administrator_user(**user)
            user.set_restaurant(restaurant_id)
        else:
            user = User.objects.create_user(**user)

        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens()
        }
