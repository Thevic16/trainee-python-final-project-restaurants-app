from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _


def validator_no_negative_no_zero(num: int) -> int:
    """
    Validate that the number is not negative, not zero

    Args:
        num (int): Input number

    Raises:
        ValidationError: The inserted number has positive

    Return:
        num (int): Input number
    """
    if num <= 0:
        raise ValidationError("The inserted number has to be positive")

    return num


def validator_ingredient_exist(filter_ingredient_count: int,
                               field: str, model: str):
    """
    Validate that the ingredient don't exist after making the appropriate query

    Args:
        filter_ingredient_count (int): Count of the ingredient in the recipe of
        the dish.
        field (str): Name field to throw error
        model (str): Name model to describe the validation error

    Raises:
        ValidationError: This ingredient has been already created
    """

    if filter_ingredient_count > 0:
        raise ValidationError({field: _('This ingredient has been already '
                                        f'created for this {model}')
                               }
                              )
