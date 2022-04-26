from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from person.models import Role
from utilities.logger import Logger


def create_role(name: str):
    try:
        created_role = Role.objects.get(name=name)
        Logger.info(f"Role '{created_role.name}' already exist in the"
                    " database")
    except ObjectDoesNotExist:
        Role.objects.create(name=name)
        Logger.info(f"Role '{name}' has been created")


class Command(BaseCommand):
    help = 'DB random roles generator'

    def handle(self, *args, **kwargs):
        try:
            create_role('Portal Manager')
            create_role('Client')
            create_role('Employee')
            create_role('Restaurant Administrator')
            create_role('Branch Manager')

        except IntegrityError:
            self.stdout.write('An error has occurred during the creation '
                              'of the roles')
