import itertools

from order.models import ItemOrder


class OrderServices:

    @staticmethod
    def get_items_order(order_id: int):
        return ItemOrder.objects.filter(order_id=order_id)

    @staticmethod
    def get_dishes_from_promotion(promotion):
        return promotion.dishes.all()

    @classmethod
    def get_all_dishes(cls, order_id: int):
        items = cls.get_items_order(order_id)
        dishes = [[item.dish]
                  if item.dish
                  else cls.get_dishes_from_promotion(item.promotion)
                  for item in items]
        return list(itertools.chain.from_iterable(dishes))

    @classmethod
    def get_total_recipes(cls, order_id: int):
        dishes = cls.get_all_dishes(order_id)
        recipes = list(itertools.chain.from_iterable(
            [dish.recipe_set.all() for dish in dishes]
        ))
        return recipes

    @staticmethod
    def get_inventory(recipe, branch_id: int):
        return recipe.ingredient.inventory_set.filter(branch_id=branch_id).first()  # noqa 501

    @classmethod
    def update_ingredients(cls, order_id: int, branch_id: int):
        recipes = cls.get_total_recipes(order_id)
        for recipe in recipes:
            inventory = cls.get_inventory(recipe, branch_id)
            inventory.availability -= recipe.quantity
            inventory.save()
