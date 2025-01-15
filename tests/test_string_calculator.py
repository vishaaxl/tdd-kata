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
        """
        Test case: Adding two numbers should return their sum.
        Input: "1,2"
        Expected Output: 3
        """
        self.assertEqual(self.calculator.add("1,2"),3)

    def test_add_multiple_numbers(self):
        """
        Test case: Adding multiple numbers should return their sum.
        Input: "1,2,3,4,5"
        Expected Output: 15
        """
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)

    def test_add_numbers_with_newlines(self):
        """
        Test case: Adding numbers separated by newlines should return their sum.
        Input: "1\n2\n3"
        Expected Output: 6
        """
        self.assertEqual(self.calculator.add("1\n2\n3"), 6)
    
    def test_add_numbers_with_custom_delimiter(self):
        """
        Test case: Adding numbers separated by a custom delimiter should return their sum.
        Input: "//;\n1;2;3"
        Expected Output: 6
        """
        self.assertEqual(self.calculator.add("//;\n1;2;3"), 6)
    
    def test_add_negative_numbers(self):
        """
        Test case: Adding numbers with negative numbers should raise an exception.
        Input: "-1,2,3"
        Expected Output: "Negative numbers are not allowed: -1"
        """
        with self.assertRaises(ValueError) as e:
            self.calculator.add("-1,2,-3")
        self.assertEqual(str(e.exception), "negative numbers are not allowed: -1, -3")

    def test_get_called_counts(self):
        """
        Test case: Calling get_called_counts method should return the number of times add method was called.
        Input: Multiple add calls
        Expected Output: 2 (if add() was called 2 times)
        """
        self.calculator.add("1,2,3")
        self.calculator.add("1,2")
        self.assertEqual(self.calculator.get_called_count(), 2)

    def test_add_numbers_greater_than_1000(self):
        """
        Test case: Numbers greater than 1000 should be ignored when calculating the sum.
        Input: "1,1001,2,3"
        Expected Output: 6
        """
        self.assertEqual(self.calculator.add("1,1001,2,3"), 6)

    def test_add_numbers_with_custom_delimiter_long_length(self):
        """
        Test case: Adding numbers separated by a custom delimiter with a long length should return their sum.
        Input: "//[***]\n1***2***3"
        Expected Output: 6
        """
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

    def test_add_numbers_with_multiple_delimiters(self):
        """
        Test case: Multiple delimiters of any length can be used.
        Input: "//[***][%%]\n1***2%%3"
        Expected Output: 6
        """
        self.assertEqual(self.calculator.add("//[***][%%]\n1***2%%3"), 6)

        