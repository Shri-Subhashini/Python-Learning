# import os 

# Decorator to handle exceptions
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            print(f"FileNotFound: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except IOError as e:
            print(f"I/O Error: {e}")
    return wrapper


class CatCommand:
    def __init__(self):
        pass

    #  Create and writing a file
    def writeFile(self, filename, file_content):
        with open(filename, 'w') as file:
            file.write(file_content)
        print(f"File created and content added in {filename} file.")
    

    # Appending a file
    def appendFile(self, filename, file_content):  
        with open(filename, 'a') as file:
            file.write(file_content + '\n')
        print(f"Content appended to the {filename} file.") 
    
    # Displaying a file
    def displayFile(self, filename):
            with open(filename, 'r') as readFile:
            print(readFile.read())

cat = CatCommand()

@handle_exceptions
def run_command(command):

    # Creating cat command object
   
    split = command.split()
    
    #If split is empty
    if not split:
        raise ValueError("Empty command")

    #Invalid command 
    if split[0] != 'cat':
        raise ValueError("Invalid command, use only cat command.")

    # For viewing filename.txt 
    if len(split) == 2:
        cat.displayFile(split[1])

    # For creating txt file
    elif len(split) >= 3 and split[1] == ">":
        content = input("Type content: ")
        cat.writeFile(split[2], content)

    # For appending txt file
    elif len(split) >= 3 and split[1] == ">>":
        content = input("Type content: ")
        cat.appendFile(split[2], content)

    else:
        raise ValueError("Invalid command")
   

while True:

    # Getting input
    catCommand = input("shell$ ")

    if catCommand.lower() == "exit":
        break
    else:
        run_command(catCommand)