from dataclasses import dataclass

from order.services import MenuServices
from utilities.auxiliaries import get_uri
from dataclasses import asdict


@dataclass
class ItemMap:
    __slots__ = ['uri', 'disable']
    uri: str
    disable: bool


@dataclass
class MenuCategoryMap:
    __slots__ = ['name', 'dishes']
    name: str
    dishes: list[ItemMap]


@dataclass
class PromotionMap:
    __slots__ = ['list_items']
    list_items: list[ItemMap]


@dataclass
class MenuMap:
    __slots__ = ['menus', 'promotions']
    menus: list[MenuCategoryMap]
    promotions: list[ItemMap]


class MapServices:
    request = None

    @classmethod
    def get_promotions_map_by_branch(cls, branch_id: int):
        list_promotions_services = MenuServices.get_menu_promotions_by_branch(
            branch_id)

        list_items = [ItemMap(
            get_uri(request=cls.request, pk=promotion_service[0],
                    model_name='promotions',
                    app_name='dish'),
            promotion_service[1]) for promotion_service in
            list_promotions_services]

        return PromotionMap(list_items)

    @classmethod
    def get_menu_category_map_by_list(cls, list_menu_category_services:
                                      list[str, list[int, bool]]):
        list_items = [ItemMap(get_uri(request=cls.request,
                                      pk=dish_service[0],
                                      model_name='dish',
                                      app_name='dish'),
                              dish_service[1]) for dish_service in
                      list_menu_category_services[1]]

        return MenuCategoryMap(list_menu_category_services[0], list_items)

    @classmethod
    def get_menus_categories_map_by_branch(cls, branch_id: int):
        list_menus_categories_services = \
            MenuServices.get_menu_dishes_by_branch(
                branch_id)

        return [cls.get_menu_category_map_by_list(
            list_menu_category_services) for list_menu_category_services in
            list_menus_categories_services]

    @classmethod
    def get_menu_map_by_branch(cls, branch_id: int):
        list_menus_categories_map = cls.get_menus_categories_map_by_branch(
            branch_id)
        promotions_map = cls.get_promotions_map_by_branch(branch_id)

        return MenuMap(menus=list_menus_categories_map,
                       promotions=promotions_map.list_items)

    @classmethod
    def get_menu_map_dict_by_branch(cls, branch_id: int):
        menu_map = cls.get_menu_map_by_branch(branch_id)
        return asdict(menu_map)
