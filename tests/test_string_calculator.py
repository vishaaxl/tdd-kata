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