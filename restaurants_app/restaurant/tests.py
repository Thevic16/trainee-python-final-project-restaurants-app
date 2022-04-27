from django.test import TestCase
from datetime import date

from dish.models import MenuCategory, Dish, Promotion
from inventory.models import Unit, Ingredient, Recipe, Inventory
from order.models import ItemOrder, Order
from restaurant import errors
from restaurant.models import (
    DeliveryType, Pay, Restaurant, FoodType, PayType, Branch)
from person.models import Person, Role
from restaurant.services import PayServices
from restaurant.validations import (
    PayDayValidator, PayValidator, RestaurantValidator)


class RestaurantAPPTestCase(TestCase):

    def setUp(self):
        # Create a restaurant
        self.food_type = FoodType(food='Test FoodType', description='Test')
        self.food_type.save()
        self.pay_type = PayType(name='Test PayType')
        self.pay_type.save()
        self.restaurant = Restaurant(name='Test Restaurant',
                                     food_type=self.food_type,
                                     active=True,
                                     pay_type=self.pay_type,
                                     max_admins=5,
                                     max_branches=5,
                                     monthly_pay=10,
                                     commission=5
                                     )
        self.restaurant.save()

        self.restaurant2 = Restaurant(name='Test Restaurant 2',
                                      food_type=self.food_type,
                                      active=True,
                                      pay_type=self.pay_type,
                                      max_admins=5,
                                      max_branches=5,
                                      monthly_pay=10,
                                      commission=5
                                      )
        self.restaurant2.save()

        # Create branches
        self.branch1 = Branch(restaurant=self.restaurant,
                              direction='Test direction 1')
        self.branch1.save()
        self.branch2 = Branch(restaurant=self.restaurant,
                              direction='Test direction 2')
        self.branch2.save()
        self.branch3 = Branch(restaurant=self.restaurant,
                              direction='Test direction 3')
        self.branch3.save()

        self.branch4 = Branch(restaurant=self.restaurant2,
                              direction='Test direction 4')
        self.branch4.save()

        # Create Menus Categories
        self.menu_category1 = MenuCategory(name='starters',
                                           restaurant=self.restaurant)
        self.menu_category1.save()
        self.menu_category2 = MenuCategory(name='meat',
                                           restaurant=self.restaurant)
        self.menu_category2.save()
        self.menu_category3 = MenuCategory(name='desserts',
                                           restaurant=self.restaurant)
        self.menu_category3.save()

        self.menu_category4 = MenuCategory(name='starters',
                                           restaurant=self.restaurant2)
        self.menu_category4.save()

        # Create Dishes
        self.dish1 = Dish(name='Dish 1', price=10, restaurant=self.restaurant,
                          menu_category=self.menu_category1)
        self.dish1.save()

        self.dish2 = Dish(name='Dish 2', price=15, restaurant=self.restaurant,
                          menu_category=self.menu_category2)
        self.dish2.save()

        self.dish3 = Dish(name='Dish 3', price=15, restaurant=self.restaurant,
                          menu_category=self.menu_category3)
        self.dish3.save()

        self.dish4 = Dish(name='Dish 4', price=15, restaurant=self.restaurant2,
                          menu_category=self.menu_category4)
        self.dish4.save()

        # Create Promotions
        self.promotion1 = Promotion(name='Promotion', price=10,
                                    since_date=date(year=2020, month=1, day=1),
                                    up_to=date(year=2020, month=1, day=15),
                                    restaurant=self.restaurant)
        self.promotion1.save()

        self.promotion1.dishes.add(self.dish1)
        self.promotion1.dishes.add(self.dish2)
        self.promotion1.dishes.add(self.dish3)

        self.promotion1.branches.add(self.branch1)

        # Create inventory
        self.unit = Unit(name='grams', abbreviation='gg')
        self.unit.save()

        self.ingredient1 = Ingredient(name='ingredient 1', unit=self.unit)
        self.ingredient1.save()
        self.ingredient2 = Ingredient(name='ingredient 2', unit=self.unit)
        self.ingredient2.save()

        self.ingredient3 = Ingredient(name='ingredient 3', unit=self.unit)
        self.ingredient3.save()

        # Create recipes for dish 1.
        self.recipe1_dish1 = Recipe(ingredient=self.ingredient1, quantity=10,
                                    dish=self.dish1)
        self.recipe1_dish1.save()

        self.recipe2_dish1 = Recipe(ingredient=self.ingredient2, quantity=10,
                                    dish=self.dish1)
        self.recipe2_dish1.save()

        # Create recipes for dish 2.
        self.recipe1_dish2 = Recipe(ingredient=self.ingredient1, quantity=10,
                                    dish=self.dish2)
        self.recipe1_dish2.save()

        # Create recipes for dish 3.
        self.recipe1_dish3 = Recipe(ingredient=self.ingredient1, quantity=10,
                                    dish=self.dish3)
        self.recipe1_dish3.save()

        # Create recipes for dish 4.
        self.recipe1_dish4 = Recipe(ingredient=self.ingredient3, quantity=10,
                                    dish=self.dish4)
        self.recipe1_dish4.save()

        # Create Inventories for branch 1
        self.inventory1_branch1 = Inventory(ingredient=self.ingredient1,
                                            availability=100,
                                            branch=self.branch1)
        self.inventory1_branch1.save()
        self.inventory2_branch1 = Inventory(ingredient=self.ingredient2,
                                            availability=100,
                                            branch=self.branch1)
        self.inventory2_branch1.save()

        # Create Inventories for branch 2
        self.inventory1_branch2 = Inventory(ingredient=self.ingredient1,
                                            availability=5,
                                            branch=self.branch2)
        self.inventory1_branch2.save()
        self.inventory2_branch2 = Inventory(ingredient=self.ingredient2,
                                            availability=5,
                                            branch=self.branch2)
        self.inventory2_branch2.save()

        self.delivery_type1 = DeliveryType(type="pick-up")
        self.delivery_type1.save()

        self.role1 = Role(name="client")
        self.role1.save()

        self.person = Person(username="Person1",
                             email="person1@persondf.com",
                             role=self.role1)
        self.person.save()

        # Create order for branch 1
        self.order1 = Order(branch=self.branch1,
                            delivery_type=self.delivery_type1,
                            direction="Cr 5 # 15 - 25",
                            client=self.person)
        self.order1.save()

        self.item_order1 = ItemOrder(quantity=3,
                                     dish=self.dish1,
                                     order=self.order1)
        self.item_order1.save()

        self.item_order2 = ItemOrder(quantity=2,
                                     dish=self.dish2,
                                     order=self.order1)
        self.item_order2.save()

        self.item_order3 = ItemOrder(quantity=1,
                                     dish=self.dish3,
                                     order=self.order1)
        self.item_order3.save()

    def test_commission_pay_case1(self):
        pay_before = len(Pay.objects.all())
        pay = PayServices.commission_pay(self.item_order1, self.order1)
        pay_after = len(Pay.objects.all())
        self.assertEqual(pay_before+1, pay_after)
        self.assertEqual(30, pay.pay)
        pay.delete()

    def test_commission_pay_case2(self):
        order2 = Order(branch=self.branch1,
                       delivery_type=self.delivery_type1,
                       direction="Cr 5 # 15 - 25",
                       client=self.person)
        order2.save()
        item_order4 = ItemOrder(quantity=2,
                                promotion=self.promotion1,
                                order=order2)
        item_order4.save()
        pay_before = len(Pay.objects.all())
        pay = PayServices.commission_pay(item_order4, order2)
        pay_after = len(Pay.objects.all())
        self.assertEqual(pay_before+1, pay_after)
        self.assertEqual(20, pay.pay)
        pay.delete()

    def test_monthtly_pay_case1(self):
        pay_before = len(Pay.objects.all())
        pay = PayServices.monthtly_pay(
            restaurant_id=self.restaurant.id,
            month_payed=1
        )
        pay_after = len(Pay.objects.all())
        self.assertEqual(pay.pay, 50)
        self.assertEqual(pay_before+1, pay_after)
        pay.delete()

    def test_commission_monthly_method_case1(self):
        with self.assertRaises(errors.NotCommissionGivenError):
            RestaurantValidator.commission_monthly_method(
                commission=None,
                pay_type="commission"
            )

    def test_commission_bte_0_100_case1(self):
        with self.assertRaises(errors.NotCommissionBte0And100):
            RestaurantValidator.commission_bte_0_100(
                commission=120
            )

    def test_commission_bte_0_100_case2(self):
        with self.assertRaises(errors.NotCommissionBte0And100):
            RestaurantValidator.commission_bte_0_100(
                commission=-10
            )

    def test_pay_day_lt_15_case1(self):
        with self.assertRaises(errors.PayDayLte15):
            PayDayValidator.pay_day_lt_15(20)

    def test_monthly_restaurant_case1(self):
        with self.assertRaises(errors.RestaurantMustBeMonthly):
            PayDayValidator.monthly_restaurant('commission')

    def test_pay_validator_case1(self):
        with self.assertRaises(errors.MonthLte12):
            PayValidator.valid_month(15)
