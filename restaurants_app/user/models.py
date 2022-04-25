from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.
from rest_framework_simplejwt.tokens import RefreshToken

from restaurant.models import Restaurant, Branch
from utilities.logger import Logger
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_client_user(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.set_role('Client')
        return user

    def create_employee_user(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.set_role('Employee')
        return user

    def create_restaurant_administrator_user(self, username, email,
                                             password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.set_role('Restaurant Administrator')
        user.is_staff = True
        return user

    def create_employee_user(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.set_role('Employee')
        user.is_staff = True
        return user


AUTH_PROVIDERS = {'google': 'google', 'email': 'email'}


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.EmailField(max_length=500)

    role = models.ForeignKey(Role, on_delete=models.CASCADE,
                             blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,
                               blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def set_password(self, password: str):
        self.password = password

    def set_role(self, role_name: str):
        role = Role.objects.get(name=role_name)
        if role:
            self.role = role
        else:
            Logger.error(f"Role '{role_name}' do not exist in the database")

    def set_restaurant(self, restaurant_id: int):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            self.restaurant = restaurant

        except ObjectDoesNotExist:
            Logger.error(f"Restaurant 'id: {restaurant_id}'"
                         f" do not exist in the database")

            raise ValidationError({'restaurant_id': _("Restaurant 'id:"
                                                      f" {restaurant_id}'"
                                                      " do not exist in the"
                                                      " database")
                                   }
                                  )

    def set_branch(self, branch_id: int):
        try:
            branch = Branch.objects.get(id=branch_id)
            self.branch = branch
        except ObjectDoesNotExist:
            Logger.error(f"Branch 'id: {branch_id}'"
                         f" do not exist in the database")
            raise ValidationError({'branch_id': _("Branch 'id:"
                                                  f" {branch_id}'"
                                                  " do not exist in the"
                                                  " database")
                                   }
                                  )

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
