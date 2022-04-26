from datetime import date

from dish.models import Dish, Promotion, MenuCategory
from inventory.models import Recipe, Inventory
from order.models import ItemOrder
from restaurant.models import Branch
from restaurant.services import PayServices


class OrderServices:

    @staticmethod
    def get_items_order(order_id: int):
        return ItemOrder.objects.filter(order_id=order_id)

    @staticmethod
    def get_dishes_from_promotion(promotion):
        return promotion.dishes.all()

    @staticmethod
    def get_inventory(recipe, branch_id: int):
        return recipe.ingredient.inventory_set.filter(branch_id=branch_id).first()  # noqa 501

    @classmethod
    def update_inventory(cls, recipes, branch_id, item_quantity):
        for recipe in recipes:
            recipe_quantity = recipe.quantity
            inventory = cls.get_inventory(recipe, branch_id)
            inventory.availability -= (recipe_quantity * item_quantity)
            inventory.save()

    @ classmethod
    def update_ingredients(cls, order):
        items = cls.get_items_order(order.id)
        for item in items:
            PayServices.commission_pay(item, order)
            item_quantity = item.quantity
            if item.promotion:
                dishes = cls.get_dishes_from_promotion(item.promotion)
                for dish in dishes:
                    recipes = dish.recipe_set.all()
                    cls.update_inventory(
                        recipes, order.branch_id, item_quantity)
                continue
            dish = item.dish
            recipes = dish.recipe_set.all()
            cls.update_inventory(recipes, order.branch_id, item_quantity)


class MenuServices:
    @ staticmethod
    def get_restaurant_by_branch(branch_id: int):
        return Branch.objects.get(id=branch_id).restaurant.id

    @ classmethod
    def get_dishes_by_branch(cls, branch_id: int):
        restaurant_id = cls.get_restaurant_by_branch(branch_id)
        return Dish.objects.filter(restaurant__id=restaurant_id,
                                   is_deleted=False)

    @ classmethod
    def get_promotion_by_branch(cls, branch_id: int):
        restaurant_id = cls.get_restaurant_by_branch(branch_id)
        return Promotion.objects.filter(restaurant__id=restaurant_id,
                                        is_deleted=False)

    @ staticmethod
    def get_recipes_by_dish(dish_id: int):
        return Recipe.objects.filter(dish__id=dish_id)

    @ staticmethod
    def get_inventory_by_ingredient_branch(ingredient_id: int,
                                           branch_id: int):
        return Inventory.objects.filter(ingredient__id=ingredient_id,
                                        branch__id=branch_id).first()

    @ staticmethod
    def compare_recipe_inventory(quantity: int, availability: int):
        if availability >= quantity:
            return True
        else:
            return False

    @ classmethod
    def verify_availability_recipe(cls, recipe_id: int, branch_id: int):
        recipe = Recipe.objects.get(id=recipe_id)
        inventory = cls.get_inventory_by_ingredient_branch(
            recipe.ingredient.id,
            branch_id)

        if inventory:
            return cls.compare_recipe_inventory(recipe.quantity,
                                                inventory.availability)
        else:
            return False

    @ classmethod
    def verify_availability_dish(cls, dish_id: int, branch_id: int):
        recipes = cls.get_recipes_by_dish(dish_id)

        for recipe in recipes:
            if not cls.verify_availability_recipe(recipe.id, branch_id):
                return False

        return True

    @ staticmethod
    def verify_promotion_branch(promotion_id: int, branch_id: int):
        promotion = Promotion.objects.get(id=promotion_id)
        list_ids_branch = [branch.id for branch in promotion.branches.all()]

        if branch_id in list_ids_branch:
            return True

        return False

    @ staticmethod
    def verify_promotion_dates(promotion_id: int):
        promotion = Promotion.objects.get(id=promotion_id)
        today = date.today()

        if promotion.since_date <= today <= promotion.up_to:
            return True

        return False

    @ classmethod
    def verify_availability_promotion(cls, promotion_id: int, branch_id: int):
        promotion = Promotion.objects.get(id=promotion_id)

        if not cls.verify_promotion_branch(promotion_id, branch_id):
            return False

        if not cls.verify_promotion_dates(promotion_id):
            return False

        for dish in promotion.dishes.all():
            if dish.is_deleted:
                return False
            if not cls.verify_availability_dish(dish.id, branch_id):
                return False

        return True

    @ classmethod
    def get_menus_categories_by_branch(cls, branch_id: int):
        restaurant_id = cls.get_restaurant_by_branch(branch_id)
        menus_categories = MenuCategory.objects.filter(
            restaurant__id=restaurant_id).all()
        return [menu_category.id for menu_category in
                menus_categories]

    @ classmethod
    def get_menu_dishes_by_branch_category(cls, branch_id: int,
                                           menu_category_id: int):
        menu_category = MenuCategory.objects.get(id=menu_category_id)
        dishes = cls.get_dishes_by_branch(branch_id).filter(
            menu_category__id=menu_category_id)

        return [menu_category.name, [[dish.id,
                                      cls.verify_availability_dish(dish.id,
                                                                   branch_id)]
                                     for dish
                                     in dishes]]

    @ classmethod
    def get_menu_dishes_by_branch(cls, branch_id: int):
        menus_categories_ids = cls.get_menus_categories_by_branch(branch_id)
        return [cls.get_menu_dishes_by_branch_category(branch_id,
                                                       menu_category_id)
                for menu_category_id in menus_categories_ids]

    @ classmethod
    def get_menu_promotions_by_branch(cls, branch_id: int):
        promotions = cls.get_promotion_by_branch(branch_id)

        return [[promotion.id,
                 cls.verify_availability_promotion(promotion.id,
                                                   branch_id)]
                for promotion
                in promotions]
