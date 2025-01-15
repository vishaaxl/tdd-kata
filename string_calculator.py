import re

class StringCalculator:
    """
    A class to implement a string calculator that can add numbers from a given string.
    The calculator supports multiple delimiters, new lines between numbers, and backward compatibility with the older format.
    
    Attributes:
    called_count (int): The count of how many times the add() method was called.
    """

    def __init__(self):
        """
        Initializes a StringCalculator instance and sets the called count to 0.
        """
        self.called_count = 0

    def add(self, numbers: str):
        """
        Adds numbers from the given string, supporting custom delimiters, multiple delimiters, 
        ignoring numbers greater than 1000, and handling negative numbers with an exception.

        The input string can use the following formats:
        1. Comma-separated values (e.g., "1,2,3")
        2. New line-separated values (e.g., "1\n2\n3")
        3. Custom delimiters defined by the user in the format `//[delimiter]\n`.

        Additionally, the method:
        - Ignores numbers greater than 1000.
        - Throws a ValueError if any negative numbers are provided.

        Parameters:
        numbers (str): A string of numbers, optionally separated by commas, new lines, or custom delimiters.

        Returns:
        int: The sum of the numbers in the input string.

        Raises:
        ValueError: If any negative numbers are found, a ValueError is raised with the message 
                    "negative numbers are not allowed" followed by the negative numbers.

        Example:
        >>> calculator = StringCalculator()
        >>> calculator.add("1,2,3")
        6

        >>> calculator.add("//[***]\n1***2***3")
        6
        """
        if not numbers:
            return 0
        
        if numbers.startswith("//"):
            delimiter_end_index = numbers.index("\n")
            delimiter_section = numbers[2:delimiter_end_index]

            if delimiter_section.startswith("["):
                delimiters = re.findall(r'\[([^\]]+)\]', delimiter_section)
            else:
                delimiters = [delimiter_section]

            numbers = numbers[delimiter_end_index + 1:]

            for delimiter in delimiters:
                numbers = numbers.replace(delimiter, ",")
        
        numbers = numbers.replace("\n", ",")

        numbers_list = numbers.split(",")
        negatives = []
        numbers_to_add = []

        for num in numbers_list:
            number = int(num)
            if number < 0:
                negatives.append(number)
            elif number > 1000:
                continue  
            else:
                numbers_to_add.append(number)

        if negatives:
            raise ValueError(f"negative numbers are not allowed: {', '.join(map(str, negatives))}")
        
        self.called_count += 1
        return sum(map(int, numbers_to_add))

    def get_called_count(self):
        """
        Returns the number of times the add() method has been invoked.

        Returns:
        int: The count of times add() has been called.
        
        Example:
        >>> calculator = StringCalculator()
        >>> calculator.add("1,2")
        >>> calculator.get_called_count()
        1
        """
        return self.called_count
