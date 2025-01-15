import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    """Test suite for the StringCalculator class."""

    def setUp(self):
        """
        Create a new instance of StringCalculator for each test.
        Can use static method to avoid creating a new instance.
        """
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        """
        Test case: Adding an empty string should return 0.
        Input: "" 
        Expected Output: 0
        """
        self.assertEqual(self.calculator.add(""), 0)

    def test_add_single_number(self):
        """
        Test case: Adding a single number should return the number itself.
        Input: "1"
        Expected Output: 1
        """
        self.assertEqual(self.calculator.add("1"), 1)

    def test_add_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"),3)