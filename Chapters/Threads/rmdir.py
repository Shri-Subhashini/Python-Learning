import os

def handle_exceptions(func):
    """
    Decorator to handle exceptions
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, *kwargs)

        except OSError as e:
            print(f"OSError: {e}")

        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")

        except PermissionError as e:
            print(f"PermissionError: {e}")
        
        except ValueError as e:
            print(f"ValueError: {e}")

    return wrapper

class RmdirCommand:

    """
    Implementation of rmdir command
    """
    def __init__(self):
        pass

    def remove_directory(self, dirname):
        """
        To remove directory
        """

        if not os.path.exists(dirname):
            print(f"Directory {dirname} not exists.")
        if not os.path.isdir(dirname):
            print(f"{dirname} is not a directory")
        os.rmdir(dirname)
        print(f"Directory {dirname} removed successfully.")

    
    def remove_parent_directory(self, dirname):
        """
        To remove parent directories also
        """

        if not os.path.exists(dirname):
            print(f"Directory {dirname} does not exists.")
        os.removedirs(dirname)
        print(f"Directory {dirname} removed successfully.")


rmdir = RmdirCommand()

@handle_exceptions
def run_command(command):
    """
    Handling inputs
    """
    split = command.split()

    if not split:
        raise ValueError("Empty command")

    if split[0] != "rmdir":
        raise ValueError("Invalid command, use rmdir only.")

    # rmdir dirname
    if len(split) == 2:
        rmdir.remove_directory(split[1])
    
    # rmdir -p dirname
    elif len(split) == 3 and split[1] == "-p":
        rmdir.remove_parent_directory(split[2])
    
    else:
        raise ValueError("Invalid syntax")


while True:
     # Getting user input
    user_input = input("skumarvel-SUBHA$ ").strip()

    if user_input.lower() == 'exit':
        break
    
    run_command(user_input)
