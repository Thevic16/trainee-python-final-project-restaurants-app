from django.core.management.base import BaseCommand
from django.db import IntegrityError
from person.models import Person
from django.core.exceptions import ValidationError
import environ
from utilities.logger import Logger
from django.core.exceptions import ObjectDoesNotExist

# Initialize environ ----------------------------------------------------------
env = environ.Env()
environ.Env.read_env()


def create_portal_manager(username: str, email: str, password: str):
    try:
        created_portal_manager = Person.objects.get(
            role__name='Portal Manager')
        Logger.info(f"Portal Manager '{created_portal_manager}' already exist"
                    f" in the database")
    except ObjectDoesNotExist:
        user = Person.objects.create_portal_manager_user(username=username,
                                                         email=email,
                                                         password=password
                                                         )
        user.is_verified = True
        user.save()
        Logger.info(f"Portal Manager has been created")


class Command(BaseCommand):
    help = 'DB random Portal Manager generator'

    def handle(self, *args, **kwargs):
        try:

            username = 'PortalManager'
            email = 'portalmanager@restaurant_app.com'
            password = env('PORTAL_MANAGER_PASSWORD')
            create_portal_manager(username=username, email=email,
                                  password=password)
        except IntegrityError:
            self.stdout.write('An error has occurred during the creation '
                              'of the roles')
        except ValidationError as e:
            Logger.error(f'ValidationError:{e}')
