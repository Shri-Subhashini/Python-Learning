import os
import stat
import time 
from datetime import datetime
from pathlib import Path
import win32security
import pywintypes


# Decorator to handle exceptions
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f"Can't find directory")  

        except PermissionError:
            print("Permission denied")

        except ValueError as e:
            print(f"Invalid value: {e}")

        except OSError as e:
            print("Error: ", e)
        
        except Exception as e:     
            print("Unexpected error:", e)
    
    return wrapper


# To get owner and group id in Windows using win32security
    def get_owner_group_windows(self, path):
        try:
            sd = win32security.GetFileSecurity(
                path,
                win32security.OWNER_SECURITY_INFORMATION |
                win32security.GROUP_SECURITY_INFORMATION)

            owner_sid = sd.GetSecurityDescriptorOwner()
            group_sid = sd.GetSecurityDescriptorGroup()

            owner, _, _ = win32security.LookupAccountSid(None, owner_sid)
            group, _, _ = win32security.LookupAccountSid(None, group_sid)

            return owner, group

        except pywintypes.error:
            return "Unknown", "Unknown"  
            

class LsCommand:
    def __init__(self):
        pass

    # Display all files and folders including hidden: ls -a
    def list_hidden_files(self, directory_path):
        files = os.listdir(directory_path)
        print('\n'.join(files))
 

    # Display all files and folders as long list : ls -l
    def long_list(self, directory_path, show_owner = True):
        for files in os.listdir(directory_path):
            full_path = os.path.join(directory_path, files)
            metadata = os.stat(full_path)
            mode  = stat.filemode(metadata.st_mode)
            size = round(metadata.st_size / 1024.0, 2)
            owner, group = self.get_owner_group_windows(full_path)
            filename = os.path.basename(files)
            date = time.ctime(metadata.st_ctime)
            input_date_format = '%a %b %d %H:%M:%S %Y'  #Format code 
            # converting string to datetime object
            date_object = datetime.strptime(date, input_date_format) 
            formatted_date_time = datetime.strftime(date_object,"%Y-%m-%d %H:%M")
            if show_owner:
                print(mode, owner, group, size, formatted_date_time, filename )
            else:
                print(mode, group, size, formatted_date_time, filename )


    # Reverse order ls -r
    def reverse_list_files(self, directory_path):
        files = os.listdir(directory_path)
        file_length = len(files)
        for i in range(file_length):
            for j in range(i+1, file_length):
                if files[i] < files[j]:
                    files[i], files[j] = files[j], files[i]
        for file in files:
            print(file)

    # Sort by modification time : ls -t
    def sort_modify_time(self, directory_path):
        files = os.listdir(directory_path)
        # files.sort(key = os.path.getmtime, reverse=True)
        file_modified_time = []
        for file in files:
            full_path = os.path.join(directory_path, file)
            mtime = os.stat(full_path).st_mtime
            # print("Mtime: ", mtime)
            file_modified_time.append([file, mtime])
            # print("Modified time: ", file_modified_time)

        file_length = len(file_modified_time)
        for i in range(file_length):
            for j in range(i+1, file_length):
                if file_modified_time[i][1] < file_modified_time[j][1]:
                    file_modified_time[i], file_modified_time[j] = file_modified_time[j], file_modified_time[i]
        for file, _ in file_modified_time:
            print(file)

    # ls -d 
    def ls_d(self, directory_path):
        if os.path.exists(directory_path):
            print(directory_path)
        else:
            print("No such file or directory")

    # Recursive listing folders and files - ls -R
    def recursive_list(self, directory_path):
        for root, sub_directories, files in os.walk(directory_path):
            print(f"\n {root}:")
            for sub_directory in sub_directories:
                print(sub_directory)
            for file in files:
                print(file)

    # ls -g
    def ls_g(self, directory_path):
        self.long_list(directory_path, show_owner=False)
        

# Creating object
lsCommand = LsCommand()

@handle_exceptions
def run_command(command):

    split = command.split()

    # Validating options
    option_list = ["-a", "-l", "-r", "-t", "-d", "-R", "-g"]
    validate_options = [option for option in split[1:] if option.startswith("-")]
    for option in validate_options:
        if option not in option_list:
            raise ValueError("Invalid command, use ls command only.")

    if not split:
        raise ValueError("Empty command")

    if split[0] != "ls":
        raise ValueError("Invalid command, use only ls command.")

    directory_path =  "." 
    
    if "-a" in split:
        lsCommand.list_hidden_files(directory_path)
    elif "-l" in split:
        lsCommand.long_list(directory_path)
    elif "-r" in split:
        lsCommand.reverse_list_files(directory_path)
    elif "-t" in split:
        lsCommand.sort_modify_time(directory_path)
    elif "-d" in split:
        index = split.index("-d")
        if len(split) > index + 1:
            directory_path = split[index + 1]
        lsCommand.ls_d(directory_path)
    elif "-R" in split:
        lsCommand.recursive_list(directory_path)
    elif "-g" in split:
        lsCommand.ls_g(".")
    else:
        for file in os.listdir(directory_path):
            print(file)

while True:

        # Getting user input
        command = input("skumarvel-SUBHA$ ").strip()

        if command == "exit":
            break
        else:
            run_command(command)

