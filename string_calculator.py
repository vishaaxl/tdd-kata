class StringCalculator:
    def add(self, numbers:str):
        if not numbers:
            return 0
        
        if numbers.startswith("//"):
            delimiter_end_index = numbers.index("\n")
            delimiter = numbers[2:delimiter_end_index]
            numbers = numbers[delimiter_end_index + 1:]
            numbers = numbers.replace(delimiter,",")
        
        numbers = numbers.replace("\n", ",")

        '''
        Split the string by commas, convert each value to an integer, 
        and sum them up
        '''
        numbers_list = map(int,numbers.split(',')) 
        return sum(numbers_list)