
# Creating a class for exception handling - Invalid number
class InvalidNumber(Exception):
    pass


# Decorator function to check if number is in range ( 0 -100000)
def validate_integer(function):
    def wrapper(self, *args, **kwargs):
        # Checking number limits
        if self.number < 0 or self.number > 100000:
            raise InvalidNumber("Number should be within 0 to 1 Lakh")
        return function(self, *args, **kwargs)
    return wrapper


# Creating number to word Conversion class
class NumberConversion:

    # Defining Constructor
    def __init__(self, number):
        self.number = number


    # Defining a integer to word conversion logic
    @validate_integer
    def int_to_word_conversion(self):

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        try:

            # Checking if number is 0 or not
            if self.number == 0:
                return "Zero"

            # Main Logic 
            words = ""

            # If number is 100000
            if self.number == 100000:
               return 'One Lakh'

            # If number is greater than 10000
            if self.number >= 10000:
                words += tens[self.number // 10000] + " "
                if self.number % 10000 == 0:
                    return words + " Thousand "
                else:
                    self.number %= 10000 

            # If number is between 1000 and 9999
            if self.number >= 1000 and self.number <= 9999:
                words += ones[self.number // 1000] + " Thousand "
                self.number %= 1000

            # If number is between 100 and 999
            if self.number >= 100 and self.number <= 999:
                words += ones[self.number // 100] + " Hundred "
                self.number %= 100

            # If number is between 10 and 19
            if self.number >= 10 and self.number <= 19:
                words += teens[self.number - 10]
                return words.strip()

            # If number is greater than 20
            if self.number >= 20:
                words += tens[self.number// 10] + " "
                self.number %= 10

            # If number is greater than 0 - likes ones digit
            if  self.number > 0:
                words += ones[self.number]

            return words.strip()

        # Handling exception for InvalidNumber
        except InvalidNumber as e:
            return e 

# Getting input from user
input_value = int(input("Enter number: "))

# Creating instances with parameter
firstInput = NumberConversion(input_value)

# Calling function on the instance
result = firstInput.int_to_word_conversion()

# Printing final result
print(f"The number is {input_value} and the word conversion is : {result}")









 # if number % 10000 == 0:
                #     return tens[number // 10000] + " Thousand "
                    
                # else:
                #     return tens[number // 10000] + " " + self.int_to_word_conversion(number % 10000)



