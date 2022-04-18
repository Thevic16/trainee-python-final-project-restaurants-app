from datetime import date

from django.test import TestCase
from django.core.exceptions import ValidationError

# Create your tests here.
from dish.validations import (validator_no_negative,
                              validate_date1_low_date2)


class DishAppTestCase(TestCase):

    def setUp(self):
        self.positive_number = 5
        self.negative_number = -5
        self.date1 = date(year=2050, month=1, day=3)
        self.date2 = date(year=2050, month=1, day=2)

    def test_validator_no_negative(self):
        self.assertEqual(self.positive_number,
                         validator_no_negative(self.positive_number))

        with self.assertRaises(ValidationError):
            validator_no_negative(self.negative_number)

    def test_validate_date1_low_date2(self):
        with self.assertRaises(ValidationError):
            validate_date1_low_date2(self.date1, self.date2, "date1", "date2")
