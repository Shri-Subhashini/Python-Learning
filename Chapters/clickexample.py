
import click
from click import Context

#Wrapper class which wraps all functions

class WrapperClass:
    
    #To validate passwred 

    def is_valid_password(self,password: str) -> list[str]:
        """
        
        To validate password by checking whether it have 1 Capital letter
        1 Small letter and 1 special character and minimum length is 8
        """
        
        #List to append errors
        errors = []
        
        #Special characters list
        special_characters = [
            "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
            "_", "+", "-", "=", "[", "]", "{", "}", "\\", 
            ";", "'", ":", "\"", ",", ".", "<", ">", 
            "/", "?", "~", "|", "`", "§", "©", "®", "™", 
            "Space", "Tab", "Enter"
        ]
        if(len(password) < 8):
            errors.append("Password must contain atleast 8 characters")
            
        has_upper = False
        has_lower = False
        has_special = False
        
        for character in password:
            ascii_character = ord(character)
            
            # To check password has 1 Upper character
            if(not has_upper and ascii_character >= 65 and ascii_character <= 90):
                has_upper = True
            
            # To check password has 1 lower character
            elif(not has_lower and ascii_character >= 97 and ascii_character <= 122):
                has_lower = True
                
            # To check password has 1 Special character
            elif(not has_special and character in special_characters):
                    has_special = True
        
        if(not has_upper):
            errors.append("Password must contain atleast 1 uppercase character")
        if(not has_lower):
            errors.append("Password must contain atleast 1 lowercase character")
        if(not has_special):
            errors.append("Password must contain atleast 1 special character")

        return errors
        
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

# Click argument parser
@click.command()
@click.option('--function', required=True, type=int, help='Function number to run')
@click.option('--password', required=False, help='Password string') 
@click.option('--listExample', 'listExample', required=False, nargs = -1, help='Comma-separated list of numbers/ characters') 
@click.option('--number', required=False, type=int, help = 'A single number input') 
@click.option('--string', required=False, help = 'String input')
@click.option('--target', required=False, type=int, help = 'Target value')
@click.option('--value', required=False, help='String or number to check palindrome')



# main function

def main(function: int, password: str | None, listExample: str | None, number: int | None, string: str | None, target: int | None, value: str | None) -> None:

    """
    To get arguments from comand line and to parse

    """

    while True:
        exit_choice = click.prompt("Would you like to exit the program? (yes/no)", type=str).lower()
        if exit_choice == "yes":
            click.echo("Exiting the program. Goodbye!")
            break 
    
    if function == 1:
        try:
            if password:
                errors = wrapper.is_valid_password(password)
                if not errors:
                    click.echo("Valid password")
                else:
                    click.echo("Invalid password:")
                    for err in errors:
                        print(f"   - {err}")
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
            click.echo(f" Error: {e}")
            

    elif function == 2:
        if listExample:
            second_largest = wrapper.second_largest_number(listExample)
            click.echo(f"Second Largest: {second_largest}" )
        else:
            listExample = click.prompt("Please enter a comma-separated list of numbers", type=int, nargs=-1)
            result = wrapper.second_largest_number(listExample)
            click.echo(f"Second largest number: {result}")
        except Exception as e:
            click.echo(f" Error: {e}")

    elif function == 3:
        if number is not None:
            wrapper.reverse_number_triangle(number)
        else:
            raise ValueError("Missing --number")
            except Exception as e:
                click.echo(f" Error: {e}")

        case 4:
            try:
                if string:
                    toggled_word = wrapper.toggle_character(string)
                    click.echo(f"Toggled Word: {toggled_word}")
                else:
                    raise ValueError("Missing --string")
            except Exception as e:
                click.echo(f" Error: {e}")

        case 5:
            try:
                if listExample:
                    chars = listExample.split(",")
                    result = wrapper.sum_up_contagious_characters(chars)
                    click.echo(f"Result: {result}")
                else:
                    raise ValueError("Missing --list")
            except Exception as e:
                print(f" Error: {e}")

        case 6:
            try:
                if listExample and target is not None:
                    numbers = listExample.split(",")
                    numbers = list(map(int, numbers))
                    result = wrapper.sum_of_indices(numbers, target)
                    click.echo(f"Indices: {result}")
                else:
                    raise ValueError("Missing --list or --target")
            except Exception as e:
                click.echo(f" Error: {e}")

        case 7:
            try:
                if value:
                    result = wrapper.is_palindrome(value)
                    click.echo("Palindrome" if result else " Not a Palindrome")
                else:
                    raise ValueError("Missing --palindromeInput")
            except Exception as e:
                click.echo(f" Error: {e}")

        case _:
            click.echo(f" Unknown function: '{function_number}'")


if __name__ == "__main__":
    
    # To print help attribute from click 
    # with Context(main) as context:
    #     click.echo(main.get_help(context))

    main()