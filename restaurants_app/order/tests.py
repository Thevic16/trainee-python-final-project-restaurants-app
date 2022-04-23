import django

django.setup()

from django.test import TestCase
from unittest.mock import patch, MagicMock
from datetime import date

from dish.models import MenuCategory, Dish, Promotion
from inventory.models import Unit, Ingredient, Recipe, Inventory
from order.map import MapServices
from restaurant.models import Restaurant, FoodType, PayType, Branch
from utilities.logger import Logger


def fake_today():
    return date(year=2020, month=1, day=5)


def fake_get_uri(request, pk: int, model_name: str, app_name: str):
    return str(pk)


# Create your tests here.
class OrderAppTestCase(TestCase):

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

    @patch('order.map.get_uri')
    @patch('order.services.date')
    def test_get_menu_map_dict_by_branch_case_1(self, mock_date, mock_get_uri):
        '''
        Test case #1 all the dishes and promotions are available for branch #1
        '''
        mock_date.today.return_value = fake_today()
        mock_get_uri.side_effect = MagicMock(side_effect=fake_get_uri)

        # Logger.debug(MapServices.get_menu_map_dict_by_branch(self.branch1.id))

        menu_dict = {'menus': [{'name': 'starters',
                                'dishes': [{'uri': '1', 'disable': True}]},
                               {'name': 'meat', 'dishes':
                                   [{'uri': '2', 'disable': True}]},
                               {'name': 'desserts',
                                'dishes': [{'uri': '3', 'disable': True}]}],
                     'promotions': [{'uri': '1', 'disable': True}]}

        self.assertEqual(menu_dict,
                         MapServices.get_menu_map_dict_by_branch(
                             self.branch1.id))

    @patch('order.map.get_uri')
    @patch('order.services.date')
    def test_get_menu_map_dict_by_branch_case_2(self, mock_date, mock_get_uri):
        '''
        Test case #2 all the dishes and promotions are not available for
         branch #2
        '''
        mock_date.today.return_value = fake_today()
        mock_get_uri.side_effect = MagicMock(side_effect=fake_get_uri)

        # Logger.debug(MapServices.get_menu_map_dict_by_branch(self.branch2.id))

        menu_dict = {'menus': [{'name': 'starters',
                                'dishes': [{'uri': '5', 'disable': False}]},
                               {'name': 'meat',
                                'dishes': [{'uri': '6', 'disable': False}]},
                               {'name': 'desserts',
                                'dishes': [{'uri': '7', 'disable': False}]}],
                     'promotions': [{'uri': '2', 'disable': False}]}

        self.assertEqual(menu_dict,
                         MapServices.get_menu_map_dict_by_branch(
                             self.branch2.id))

    @patch('order.map.get_uri')
    @patch('order.services.date')
    def test_get_menu_map_dict_by_branch_case_3(self, mock_date, mock_get_uri):
        '''
         Test case #3 all create recipe for dish 4 but there is not inventory
          for that recipe in branch #4 and promotion is out of date
         '''
        mock_date.today.return_value = fake_today()
        mock_get_uri.side_effect = MagicMock(side_effect=fake_get_uri)

        # Create Promotions
        self.promotion2 = Promotion(name='Promotion 2', price=10,
                                    since_date=date(year=2019, month=2, day=1),
                                    up_to=date(year=2019, month=2, day=15),
                                    restaurant=self.restaurant2)
        self.promotion2.save()
        self.promotion2.dishes.add(self.dish4)
        self.promotion2.branches.add(self.branch4)

        Logger.debug(MapServices.get_menu_map_dict_by_branch(self.branch4.id))

        menu_dict = {'menus': [{'name': 'starters',
                                'dishes': [{'uri': '12', 'disable': False}]}],
                     'promotions': [{'uri': '4', 'disable': False}]}

        self.assertEqual(menu_dict,
                         MapServices.get_menu_map_dict_by_branch(
                             self.branch4.id))
