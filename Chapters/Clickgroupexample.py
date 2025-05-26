

import re
import sys
import click

#Wrapper class which wraps all functions

class WrapperClass:
   
    #To validate passwred

    def is_valid_password(self,password: str) -> list[str]:
        """
       
        To validate password by checking whether it have 1 Capital letter
        1 Small letter and 1 special character and minimum length is 8
        """

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
        if not re.match(pattern, password):
            raise ValueError("Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (@#$%^&+=!).")
       
           
    #To find Second largest number in a list

    def second_largest_number(self, numbers: list[int]) -> int:
       
        """ Returns the second largest number in the list """
     
        if len(numbers) < 2:
            raise ValueError("List must contain at least two numbers.")
       
        input_length = len(numbers)
        for i in range(2):
            for j in range(0, input_length-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers[-2]


    # Pattern - triangle_reverse number

    def reverse_number_triangle(self, number: int)-> None:
       
        """ Print a reverse number triangle pattern """
        
        if number <= 0:
            raise ValueError("Number must be positive.")
       
        for i in range(1, number+1):
            for j in range(i, 0, -1):
                print(j, end = " ")
            print()


    #To toggle a word

    def toggle_character(self, input_string: str) -> str:
        """
        To toggle the word into uppercase and lowercase
        """
       
        toggled_word = ""
        for character in input_string:
            ascii_character = ord(character)
        
            # To check whether it's uppercase
            if(ascii_character >= 65 and ascii_character <= 90):
                toggled_word += chr(ascii_character + 32)
        
            #To check whether it's lowercase
            elif(ascii_character >= 97 and ascii_character <= 122):
                toggled_word += chr(ascii_character - 32)
            
            # For non-alphabets keep as such
            else:
                toggled_word += character
        return toggled_word
       


    #Sum of Contagious Character

    def sum_up_contagious_characters(self, input_list: list[str]) -> list[str]:
       
        """
        Sum up the contagious character in the list
        """
       
        if not input_list or all(c.strip() == '' for c in input_list):
            raise ValueError("List cannot be empty.")
       
        outputList = []
        i = 0
        while(i < len(input_list)-1):
            j = i+1
            sum_of_characters = 1
            while(j < len(input_list)):
                if(input_list[i] == input_list[j]):
                    sum_of_characters += 1
                    i = j
                    j = j+1
                    continue

                # To print last and before element,if not contagious element present
                elif(j == len(input_list)-1):
                    outputList.append(str(sum_of_characters) + input_list[i])
                    outputList.append(str(sum_of_characters) + input_list[j])
                    j += 1
                    i = j
                else:
                    outputList.append(str(sum_of_characters) + input_list[i])
                    i = j
                    break
       
        return outputList
 
           
    #To get the sum of indicies of given list which matches the target
   
    def sum_of_indices(self, input_list: list[int], target: int) -> list[int]:
        """
            Recursive approach to find indices of elements in the list
            that sum up to the target.
        """
        def recursiveFunction(start: int, current_sum: int, indices: list[int]) ->list[int] | None:
            if current_sum == target:
                return indices
            if current_sum > target:
                return None
           
            for i in range(start, len(input_list)):
                result = recursiveFunction(i + 1, current_sum + input_list[i], indices + [i])
                if result:
                    return result
            return None

        if len(input_list) < 2:
            raise ValueError("List must contain at least two elements.")

        result = recursiveFunction(0, 0, [])
        if result:
            return result
        else:
            raise ValueError("No indices found.")
           
    # To check the given string / number is a palindrome or not

    def is_palindrome(self, value: str | int) -> bool:
        """
        Checks if the given value is palindrome or not
        """
       
        value_into_string = str(value)
        reversed_value = ""

        for character in value_into_string:
            reversed_value = character + reversed_value
           
        return reversed_value == value_into_string
 

#Creating a instance for the class

wrapper = WrapperClass()

# main function


"""
To get arguments from comand line and to parse

"""
    
@click.group()
def cli():
    """CLI group for various utility functions."""
    pass

@cli.command()
@click.option('--password', required=False, help='Password string', default='')
def validate(password):
    """Validate a password."""
    
    try:
        if password:
            errors = wrapper.is_valid_password(password)
            if not errors:
                click.echo("Valid password")
            else:
                click.echo("Invalid password:")
                for err in errors:
                    click.echo(f"  - {err}")
        else:
            password = click.prompt("Please enter your password", type=str)
            errors = wrapper.is_valid_password(password)
        if not errors:
            click.echo("Valid password")
        else:
            click.echo("Invalid password:")
            for err in errors:
                click.echo(f"  - {err}")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument('listexample', nargs=-1)
def second_largest(listexample):
    """Find the second largest number in a list."""
    
    try:
        if listexample:
            listexample = [int(x.strip()) for x in listexample]
            second_largest = wrapper.second_largest_number(listexample)
            click.echo(f"Second Largest: {second_largest}")
        else:
            listexample = click.prompt("Please enter a space-separated list of numbers")
            listexample = [int(x.strip()) for x in listexample.split()]
            result = wrapper.second_largest_number(listexample)
            click.echo(f"Second largest number: {result}")
    except Exception as e:
        click.echo(f"Error: {e}")
        
@cli.command()
@click.argument('listexample', nargs=-1)
def sum_contiguous(listexample):
    """Sum up contiguous characters in a list."""
    
    try:
        if listexample:
            result = wrapper.sum_up_contagious_characters(listexample)
            click.echo(f"Result: {result}")
        else:
            listexample = click.prompt("Please enter a space-separated list of characters")
            result = wrapper.sum_up_contagious_characters(listexample)
            click.echo(f"Result: {result}")
    except Exception as e:
        click.echo(f"Error: {e}")
        
@cli.command()
@click.argument('listexample', nargs=-1)
@click.option('--target', required=False, type=int, help='Target value')
def sum_indices(listexample, target):
    """Find indices of elements that sum up to the target."""

    try:
        if listexample:
            listexample = [int(x) for x in listexample]
            result = wrapper.sum_of_indices(listexample, target)
            click.echo(f"Indices: {result}")
        else:
            listexample = click.prompt("Please enter a space-separated list of numbers")
            listexample = [int(x) for x in listexample.split()]
            target = click.prompt("Please enter the target sum", type=int)
            result = wrapper.sum_of_indices(listexample, target)
            click.echo(f"Indices: {result}")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.option('--string', required=False, help='String input', default='')
def toggle_case(string):
    """Toggle the case of a string."""
    
    try:
        if string:
            toggled_word = wrapper.toggle_character(string)
            click.echo(f"Toggled Word: {toggled_word}")
        else:
            string = click.prompt("Please enter a string", type=str)
            toggled = wrapper.toggle_character(string)
            click.echo(f"Toggled string: {toggled}")
    except Exception as e:
        click.echo(f"Error: {e}")
    
@cli.command()
@click.option('--value', required=False, help='String or number to check palindrome', default='')
def palindrome(value):
    """Check if a string or number is a palindrome."""
    
    try:
        if value:
            result = wrapper.is_palindrome(value)
            click.echo("Palindrome" if result else "Not a Palindrome")
        else:
            value = click.prompt("Please enter a string or number to check for palindrome", type=str)
            result = wrapper.is_palindrome(value)
            click.echo("Palindrome" if result else "Not a palindrome")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.option('--number', required=False, type=int, help='A single number input')
def reverse_triangle(number):
    
    try:
        if number is not None:
            wrapper.reverse_number_triangle(number)
        else:
            number = click.prompt("Please enter a number", type=int)
            wrapper.reverse_number_triangle(number)
    except Exception as e:
        click.echo(f"Error: {e}")


if __name__ == "__main__":   
    cli()


'''

import re
import sys
import click

#Wrapper class which wraps all functions

class WrapperClass:
   
    #To validate passwred

    def is_valid_password(self,password: str) -> list[str]:
        """
       
        To validate password by checking whether it have 1 Capital letter
        1 Small letter and 1 special character and minimum length is 8
        """

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
        if not re.match(pattern, password):
            raise ValueError("Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (@#$%^&+=!).")
       
           
    #To find Second largest number in a list

    def second_largest_number(self, numbers: list[int]) -> int:
       
        """ Returns the second largest number in the list """
     
        if len(numbers) < 2:
            raise ValueError("List must contain at least two numbers.")
       
        input_length = len(numbers)
        for i in range(2):
            for j in range(0, input_length-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers[-2]


    # Pattern - triangle_reverse number

    def reverse_number_triangle(self, number: int)-> None:
       
        """ Print a reverse number triangle pattern """
        
        if number <= 0:
            raise ValueError("Number must be positive.")
       
        for i in range(1, number+1):
            for j in range(i, 0, -1):
                print(j, end = " ")
            print()


    #To toggle a word

    def toggle_character(self, input_string: str) -> str:
        """
        To toggle the word into uppercase and lowercase
        """
       
        toggled_word = ""
        for character in input_string:
            ascii_character = ord(character)
        
            # To check whether it's uppercase
            if(ascii_character >= 65 and ascii_character <= 90):
                toggled_word += chr(ascii_character + 32)
        
            #To check whether it's lowercase
            elif(ascii_character >= 97 and ascii_character <= 122):
                toggled_word += chr(ascii_character - 32)
            
            # For non-alphabets keep as such
            else:
                toggled_word += character
        return toggled_word
       


    #Sum of Contagious Character

    def sum_up_contagious_characters(self, input_list: list[str]) -> list[str]:
       
        """
        Sum up the contagious character in the list
        """
       
        if not input_list or all(c.strip() == '' for c in input_list):
            raise ValueError("List cannot be empty.")
       
        outputList = []
        i = 0
        while(i < len(input_list)-1):
            j = i+1
            sum_of_characters = 1
            while(j < len(input_list)):
                if(input_list[i] == input_list[j]):
                    sum_of_characters += 1
                    i = j
                    j = j+1
                    continue

                # To print last and before element,if not contagious element present
                elif(j == len(input_list)-1):
                    outputList.append(str(sum_of_characters) + input_list[i])
                    outputList.append(str(sum_of_characters) + input_list[j])
                    j += 1
                    i = j
                else:
                    outputList.append(str(sum_of_characters) + input_list[i])
                    i = j
                    break
       
        return outputList
 
           
    #To get the sum of indicies of given list which matches the target
   
    def sum_of_indices(self, input_list: list[int], target: int) -> list[int]:
        """
            Recursive approach to find indices of elements in the list
            that sum up to the target.
        """
        def recursiveFunction(start: int, current_sum: int, indices: list[int]) ->list[int] | None:
            if current_sum == target:
                return indices
            if current_sum > target:
                return None
           
            for i in range(start, len(input_list)):
                result = recursiveFunction(i + 1, current_sum + input_list[i], indices + [i])
                if result:
                    return result
            return None

        if len(input_list) < 2:
            raise ValueError("List must contain at least two elements.")

        result = recursiveFunction(0, 0, [])
        if result:
            return result
        else:
            raise ValueError("No indices found.")
           
    # To check the given string / number is a palindrome or not

    def is_palindrome(self, value: str | int) -> bool:
        """
        Checks if the given value is palindrome or not
        """
       
        value_into_string = str(value)
        reversed_value = ""

        for character in value_into_string:
            reversed_value = character + reversed_value
           
        return reversed_value == value_into_string
 

#Creating a instance for the class

wrapper = WrapperClass()

# main function
def main() -> None:

    """
    To get arguments from comand line and to parse

    """
    def handle_function():
       
        @click.group()
        def cli():
            """CLI group for various utility functions."""
            pass

        @cli.group()
        def password_group():
            """Group for password-related operations."""
            pass

        @password_group.command()
        @click.option('--password', required=False, help='Password string', default='')
        def validate(password):
            """Validate a password."""
            while True:
                try:
                    if password:
                        errors = wrapper.is_valid_password(password)
                        if not errors:
                            click.echo("Valid password")
                        else:
                            click.echo("Invalid password:")
                            for err in errors:
                                click.echo(f"  - {err}")
                    else:
                        password = click.prompt("Please enter your password", type=str)
                        errors = wrapper.is_valid_password(password)
                    if not errors:
                        click.echo("Valid password")
                    else:
                        click.echo("Invalid password:")
                        for err in errors:
                            click.echo(f"  - {err}")
                except Exception as e:
                    click.echo(f"Error: {e}")
                finally:
                    execute_again = click.prompt("Would you like to execute another input? (yes/no)", type=str).lower()
                    if execute_again != "yes":
                        break
                    password = None
            prompt_exit_choice()

        @cli.group()
        def list_operations():
            """Group for list-related operations."""
            pass

        @list_operations.command()
        @click.argument('listexample', nargs=-1)
        def second_largest(listexample):
            """Find the second largest number in a list."""
            while True:
                try:
                    if listexample:
                        listexample = [int(x.strip()) for x in listexample]
                        second_largest = wrapper.second_largest_number(listexample)
                        click.echo(f"Second Largest: {second_largest}")
                    else:
                        listexample = click.prompt("Please enter a space-separated list of numbers")
                        listexample = [int(x.strip()) for x in listexample.split()]
                        result = wrapper.second_largest_number(listexample)
                        click.echo(f"Second largest number: {result}")
                except Exception as e:
                    click.echo(f"Error: {e}")
                finally:
                    execute_again = click.prompt("Would you like to execute another input? (yes/no)", type=str).lower()
                    if execute_again != "yes":
                        break
                    listexample = None
            prompt_exit_choice()

        @list_operations.command()
        @click.argument('listexample', nargs=-1)
        def sum_contiguous(listexample):
            """Sum up contiguous characters in a list."""
            while True:
                try:
                    if listexample:
                        result = wrapper.sum_up_contagious_characters(listexample)
                        click.echo(f"Result: {result}")
                    else:
                        listexample = click.prompt("Please enter a space-separated list of characters")
                        result = wrapper.sum_up_contagious_characters(listexample)
                        click.echo(f"Result: {result}")
                except Exception as e:
                    click.echo(f"Error: {e}")
                finally:
                    execute_again = click.prompt("Would you like to execute another input? (yes/no)", type=str).lower()
                    if execute_again != "yes":
                        break
                    listexample = None
            prompt_exit_choice()

        @list_operations.command()
        @click.argument('listexample', nargs=-1)
        @click.option('--target', required=False, type=int, help='Target value')
        def sum_indices(listexample, target):
            """Find indices of elements that sum up to the target."""
            while True:
                try:
                    if listexample:
                        listexample = [int(x) for x in listexample]
                        result = wrapper.sum_of_indices(listexample, target)
                        click.echo(f"Indices: {result}")
                    else:
                        listexample = click.prompt("Please enter a space-separated list of numbers")
                        listexample = [int(x) for x in listexample.split()]
                        target = click.prompt("Please enter the target sum", type=int)
                        result = wrapper.sum_of_indices(listexample, target)
                        click.echo(f"Indices: {result}")
                except Exception as e:
                    click.echo(f"Error: {e}")
                finally:
                    execute_again = click.prompt("Would you like to execute another input? (yes/no)", type=str).lower()
                    if execute_again != "yes":
                        break
                    listexample = None
                    target = None
            prompt_exit_choice()

        @cli.group()
        def string_operations():
            """Group for string-related operations."""
            pass

        @string_operations.command()
        @click.option('--string', required=False, help='String input', default='')
        def toggle_case(string):
            """Toggle the case of a string."""
            while True:
                try:
                    if string:
                        toggled_word = wrapper.toggle_character(string)
                        click.echo(f"Toggled Word: {toggled_word}")
                    else:
                        string = click.prompt("Please enter a string", type=str)
                        toggled = wrapper.toggle_character(string)
                        click.echo(f"Toggled string: {toggled}")
                except Exception as e:
                    click.echo(f"Error: {e}")
                finally:
                    execute_again = click.prompt("Would you like to execute another input? (yes/no)", type=str).lower()
                    if execute_again != "yes":
                        break
                    string = None
            prompt_exit_choice()

        @string_operations.command()
        @click.option('--value', required=False, help='String or number to check palindrome', default='')
        def palindrome(value):
            """Check if a string or number is a palindrome."""
            while True:
                try:
                    if value:
                        result = wrapper.is_palindrome(value)
                        click.echo("Palindrome" if result else "Not a Palindrome")
                    else:
                        value = click.prompt("Please enter a string or number to check for palindrome", type=str)
                        result = wrapper.is_palindrome(value)
                        click.echo("Palindrome" if result else "Not a palindrome")
                except Exception as e:
                    click.echo(f"Error: {e}")
                finally:
                    execute_again = click.prompt("Would you like to execute another input? (yes/no)", type=str).lower()
                    if execute_again != "yes":
                        break
                    value = None
            prompt_exit_choice()

        @cli.group()
        def pattern_operations():
            """Group for pattern-related operations."""
            pass

        @pattern_operations.command()
        @click.option('--number', required=False, type=int, help='A single number input')
        def reverse_triangle(number):
            """Print a reverse number triangle."""
            while True:
                try:
                    if number is not None:
                        wrapper.reverse_number_triangle(number)
                    else:
                        number = click.prompt("Please enter a number", type=int)
                        wrapper.reverse_number_triangle(number)
                except Exception as e:
                    click.echo(f"Error: {e}")
                finally:
                    execute_again = click.prompt("Would you like to execute another input? (yes/no)", type=str).lower()
                    if execute_again != "yes":
                        break
                    number = None
            prompt_exit_choice()
        
        def prompt_exit_choice():
            exit_choice = click.prompt("Would you like to exit the program? (yes/no)", type=str).lower()
            if exit_choice != "no":
                sys.exit(1)
            sys.argv = sys.argv[:1]
            handle_function()

        if __name__ == "__main__":
            cli()
        
    handle_function()

if __name__ == "__main__":   
    main()

'''












