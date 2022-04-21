from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, m2m_changed

from dish.validations import validator_no_negative, validate_date1_low_date2
from inventory.validations import validator_field_exist, validator_ids, \
    validator_ids_list
from restaurant.models import Restaurant, Branch
from utilities.logger import Logger


def upload_dish_image(instance, file_name):
    return f'dishes/{instance.name}/{file_name}'


class MenuCategory(models.Model):
    name = models.CharField(max_length=120)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} (Restaurant: {self.restaurant.name})'


def menu_category_model_pre_save_receiver(sender, instance, *args, **kwargs):
    try:
        # Update
        pre_save_menu = MenuCategory.objects.get(id=instance.id)
        if pre_save_menu:
            Logger.info(f'menu_category (id:{pre_save_menu.id} has been'
                        f' updated)')

    except ObjectDoesNotExist:
        validator_field_exist(MenuCategory.objects.filter(
            name=instance.name,
            restaurant__id=instance.restaurant.id).count(),
                              'name', 'restaurant')

        Logger.info(f'Create inventory first time, will be necessary to'
                    f' validate')


pre_save.connect(menu_category_model_pre_save_receiver, sender=MenuCategory)


class Dish(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                validators=[validator_no_negative])
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to=upload_dish_image, null=True,
                              blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} (Restaurant: {self.restaurant.name})'


def dish_model_pre_save_receiver(sender, instance, *args, **kwargs):
    try:
        # Update
        pre_save_dish = Dish.objects.get(id=instance.id)
        validator_ids(pre_save_dish.restaurant.id,
                      pre_save_dish.menu_category.restaurant.id, "restaurant",
                      'menu_category')
        if pre_save_dish:
            Logger.info(f'dish (id:{pre_save_dish.id} has been'
                        f' updated)')

    except ObjectDoesNotExist:
        validator_field_exist(Dish.objects.filter(
            name=instance.name,
            restaurant__id=instance.restaurant.id).count(),
                              'name', 'restaurant')

        validator_ids(instance.restaurant.id,
                      instance.menu_category.restaurant.id, "restaurant",
                      'menu_category')

        Logger.info(f'Create dish first time, will be necessary to'
                    f' validate')


pre_save.connect(dish_model_pre_save_receiver, sender=Dish)


class Promotion(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                validators=[validator_no_negative])
    since_date = models.DateField(null=True, blank=True)
    up_to = models.DateField(null=True, blank=True)
    dishes = models.ManyToManyField(Dish)
    branches = models.ManyToManyField(Branch)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def promotion_model_pre_save_receiver(sender, instance, *args,
                                      **kwargs):
    validate_date1_low_date2(instance.since_date, instance.up_to,
                             'since_date', 'up_to')


def promotion_dishes_m2m_changed_receiver(sender, instance, action, *args,
                                         **kwargs):
    if action == 'post_add' or action == 'post_remove':
        Logger.debug(f'dishes: '
                     f'{instance.dishes}')

        validator_ids_list(
            [dish.restaurant.id for dish in instance.dishes.all()] +
            [branch.restaurant.id for branch in
             instance.branches.all()],
            'dishes',
            'branches')


def promotion_branches_m2m_changed_receiver(sender, instance, action, *args,
                                         **kwargs):
    if action == 'post_add' or action == 'post_remove':
        Logger.debug(f'branches: '
                     f'{instance.branches}')

        validator_ids_list(
            [dish.restaurant.id for dish in instance.dishes.all()] +
            [branch.restaurant.id for branch in
             instance.branches.all()],
            'dishes',
            'branches')


pre_save.connect(promotion_model_pre_save_receiver, sender=Promotion)
m2m_changed.connect(promotion_dishes_m2m_changed_receiver,
                    sender=Promotion.dishes.through)
m2m_changed.connect(promotion_branches_m2m_changed_receiver,
                    sender=Promotion.branches.through)
