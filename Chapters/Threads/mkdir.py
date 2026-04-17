import os

def handle_exceptions(func):
    """
    Decorator to handle exceptions
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, *kwargs)

        except FileExistsError as e:
            print(f"FileExistsError: {e}")

        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")

        except PermissionError as e:
            print(f"PermissionError: {e}")
        
        except ValueError as e:
            print(f"ValueError: {e}")

    return wrapper


class MkdirCommand:
    """
    Implementation of mkdir command 
    """

    def __init__(self):
        pass
    

    def create_directory(self, dirname):
        """
        Create directory using os.mkdir()
        """
        if os.path.exists(dirname):
            print(f"Directory {dirname} already exists")
        os.mkdir(dirname)
        print(F"Directory {dirname} created successfully.")

    
    def create_parent_directory(self, dirname):
        """
        Create parent directory if it does not exist
        """

        os.makedirs(dirname, exist_ok = True)
        print(f"Directory path {dirname} created.")


# Creating mkdir object
mkdir = MkdirCommand()

@handle_exceptions
def run_command(command):
    """
    Handling inputs
    """

    split = command.split()
    if not split:
        raise ValueError("Empty command")
    
    if split[0] != "mkdir":
        raise ValueError("Invalid command, use only mkdir.")
    
    # mkdir dirname
    if len(split) == 2:
        mkdir.create_directory(split[1])

    # mkdir -p dirname
    elif len(split) == 3 and split[1] == '-p':
        mkdir.create_parent_directory(split[2])

    else:
        raise ValueError("Invalid syntax.")


while True:
    
    # Getting user input
    user_input = input("skumarvel-SUBHA$ ").strip()

    if user_input.lower() == 'exit':
        break
    
    run_command(user_input)