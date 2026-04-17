# Decorator function to check if number is in range ( 0 -100000)
def validate_integer(function):
    def wrapper(self, *args, **kwargs):
        # Checkingnumberumber limits
        if self.number < 0 or self.number > 100000:
            raise InvalidNumber("Number should be within 0 to 1 Lakh")
        return function(self, *args, **kwargs)
    return wrapper


# Creating a class for exception handling - Invalidnumberumber
class InvalidNumber(Exception):
    pass


# Creating number to word Conversion class
class numberConversion:

    # Defining Constructor
    def __init__(self,number):
        self.number =number


    # Defining a integer to word conversion logic
    @validate_integer
    def int_to_word_conversion(self, number):
        try:
            # Checking if number is 0 or not
            if number == 0:
                return ""

            ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

            words = ""

            # If number is 100000
            if self.number == 100000:
               return 'One Lakh'

            # If number is greater than 10,000
            if number >= 10000:
                return self.int_to_word_conversion(number // 1000) + " Thousand " + self.int_to_word_conversion(number % 1000)

            # If number is greater than 1000
            if number >= 1000:
                return ones[number // 1000] + " Thousand " + self.int_to_word_conversion(number % 1000)

            # If number is greater than 100
            if number >= 100:
                return ones[number // 100] + " Hundred " + self.int_to_word_conversion(number % 100)

            # If number is between 10 - 19
            if 10 <= number <= 19:
                return teens[number - 10]

            # If number is greater than 20
            if number >= 20:
                return tens[number // 10] + " " + self.int_to_word_conversion(number % 10)

            # If number is greater than 0
            if  number > 0:
                return ones[number]
        
        # Handling exception for InvalidNumber
        except InvalidNumber as e:
            return e 


while True:

    # Getting input from user
    input_value = input("Enter number (or type 'exit' to quit): ")

    # To exit loop
    if input_value.lower() == 'exit':
        print("Program terminated...")
        break

    input_value = int(input_value)

   
    # Creating instances with parameter
    firstInput = numberConversion(input_value)

    # Calling function on the instance
    result = firstInput.int_to_word_conversion(firstInput.number)

    # Printing final result
    print(f"The number is {input_value} and the word conversion is : {result}")



# print(234//10)    23
# print(234%10)     4
# print(2345//100)  23
# print(2345%100)   45
# print(2345 //1000) 2
# print(2345%1000)   345