from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from utilities.logger import Logger


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


def validator_field_exist(field_count: int,
                          field: str, model: str):
    """
    Validate that the ingredient don't exist after making the appropriate query

    Args:
        field_count (int): Count of the field in the model for a restaurant
        field (str): Name field to throw error
        model (str): Name model to describe the validation error

    Raises:
        ValidationError: This ingredient has been already created
    """

    if field_count > 0:
        raise ValidationError({field: _('This field has been already '
                                        f'created for this {model}')
                               }
                              )


def validator_ids(id1: int, id2: int,
                  field1: str, field2: str):
    """
    Validate that both ids are the same

    Args:
        id1 (int): Id1 to compare
        id2 (int): Id2 to compare
        field1 (str): Name field1 to compare
        field2 (str): Name field2 to compare

    Raises:
        ValidationError: The ids are not the same
    """

    if id1 != id2:
        raise ValidationError({field1: _(f"The fields {field1} and {field2} "
                                         "don't belong to the same"
                                         " restaurant")
                               }
                              )


def validator_ids_list(list_ids: list[int],
                       field1: str, field2: str):
    """
    Validate that all ids are the same

    Args:
        list_ids (list[int]): List of ids to compare
        field1 (str): Name field1 to compare
        field2 (str): Name field2 to compare

    Raises:
        ValidationError: The ids are not the same
    """
    Logger.info(f'list_ids: {list_ids}')

    if (len_list := len(list_ids)) > 0:
        if len_list != list_ids.count(list_ids[0]):
            raise ValidationError({field1: _(f"The fields {field1} and "
                                             f"{field2} "
                                             "don't belong to the same"
                                             " restaurant")
                                   }
                                  )
