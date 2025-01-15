class StringCalculator:
    def add(self, numbers:str):
        if not numbers:
            return 0
        '''
        Split the string by commas, convert each value to an integer, 
        and sum them up
        '''
        numbers_list = map(int,numbers.split(',')) 
        return sum(numbers_list)