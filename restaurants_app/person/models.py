from django.db import models
from restaurant.models import Restaurant, Branch


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    identification = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.identification})'
