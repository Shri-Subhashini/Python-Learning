
from nodes.fileResolve import FileResolve
from nodes.node import Node
from commands.ls import LsCommand
from commands.cd import CdCommand
from commands.find import FindCommand
from commands.cat import CatCommand
from commands.mkdir import MkdirCommand
from commands.rm import RmCommand
from commands.rmdir import RmdirCommand


# Creating object for FileResolve.py
fileresolve = FileResolve()

# Creating object for each commands 
commands = {
    "ls": LsCommand,
    "cd": CdCommand,
    "cat": CatCommand,
    "mkdir": MkdirCommand,
    "find": FindCommand,
    "rmdir": RmdirCommand,
    "rm": RmCommand,
}

while True:
    command_input = input(f"VFS:{fileresolve.printWorkingDirectory()}$ ").strip()

    if not command_input:
        continue

    if command_input == "exit":
        break

    parts = command_input.split()
    command = parts[0]  # First word in command_input
    arguments = parts[1:]  #Remaining words in command_input

    if command in commands:
        try:
            # Calling respective command class with their objects
            commands[command]().run(fileresolve, arguments)
        except Exception as e:
            print("Error: ", e)
    else:
        print("Command not found")