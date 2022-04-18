from django.test import TestCase
from django.core.exceptions import ValidationError


# Create your tests here.
from inventory.validations import validator_no_negative_no_zero


class DishAppTestCase(TestCase):

    def setUp(self):
        self.positive_number = 5
        self.zero_number = 0
        self.negative_number = -5

    def test_validator_no_negative_no_zero(self):
        self.assertEqual(self.positive_number,
                         validator_no_negative_no_zero(self.positive_number))

        with self.assertRaises(ValidationError):
            validator_no_negative_no_zero(self.zero_number)

        with self.assertRaises(ValidationError):
            validator_no_negative_no_zero(self.negative_number)


