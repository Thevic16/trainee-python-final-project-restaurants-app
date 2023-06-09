from person.models import Person
import os
import random
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from utilities.logger import Logger


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    if not Person.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def authenticate(email: str, password: str):
    user = Person.objects.filter(email=email, password=password).first()

    if user:
        return user
    else:
        raise AuthenticationFailed


def register_social_user(provider: str, user_id: int, email: str, name: str,
                         user_role: str, restaurant_id: int, branch_id: int):
    filtered_user_by_email = Person.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:

            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            Logger.debug(f'registered_user: {registered_user}')

            return {
                'username': registered_user.username,
                'email': registered_user.email,
                'role': registered_user.role.name,
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
            user = Person.objects.create_client_user(**user)
        elif user_role == 'Restaurant Administrator':
            user = Person.objects.create_restaurant_administrator_user(**user)
            user.set_restaurant(restaurant_id)
        elif user_role == 'Employee':
            user = Person.objects.create_employee_user(**user)
            user.set_branch(branch_id)
        elif user_role == 'Branch Manager':
            user = Person.objects.create_branch_manager_user(**user)
            user.set_branch(branch_id)
        else:
            raise ValidationError({"auth_token": _('The user that has been '
                                                   'passed through the token '
                                                   'does not exist in the '
                                                   'database.')
                                   }
                                  )

        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'role': new_user.role.name,
            'tokens': new_user.tokens()
        }


def authenticate_portal_manager(email: str, password: str):
    user = authenticate(email, password)

    return {
        'email': user.email,
        'username': user.username,
        'role': user.role.name,
        'tokens': user.tokens()
    }
