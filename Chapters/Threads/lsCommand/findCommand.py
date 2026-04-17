import os
from typing import List, Optional
import fnmatch
import win32security
import pywintypes


# Decorator to handle exceptions
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except FileNotFoundError:
            print("Can't find directory")

        except PermissionError:
            print("Permission denied")

        except ValueError as e:
            print(f"Invalid value: {e}")

        except OSError as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected error:", e)
    return wrapper


def validate_path(path):
    """
    Validates whether the given path exists.
    Raises ValueError if path is invalid.
    """

    if not os.path.exists(path):
        raise ValueError(f"Path does not exist: {path}")

class findCommand:
    """
    Implementation of find command
    """

    def __init__(self):
        pass

    # ACL for windows
    def get_owner_windows(self, path):
        try:
            sd = win32security.GetFileSecurity(
                path,
                win32security.OWNER_SECURITY_INFORMATION
            )
            owner_sid = sd.GetSecurityDescriptorOwner()
            owner, _, _ = win32security.LookupAccountSid(None, owner_sid)
            return owner
        except pywintypes.error:
            return None

    # Requirement to check the arguments
    def require_argument(self, split, index, option):
        if index + 1 >= len(split):
            raise ValueError("Invalid find syntax")


    @handle_exceptions
    def find_name(self, path: str, filename: str, fileType: Optional[str] = None):
        """
        Find files by exact name
        """

        for root, dirs, files in os.walk(path):
            if fileType == 'd':
                target = dirs 
            else:
                target = files
            for name in target:
                if fnmatch.fnmatch(name, filename):
                    print(os.path.join(root, name))


    @handle_exceptions
    def find_iname(self, path:str, filename:str, fileType: Optional[str] = None):
        """
        Find files by name - case-insensitive
        """

        filename = filename.lower()
        for root, _ , files in os.walk(path):
            target = files if fileType == "f" or fileType is None else directory
            for name in target:
                if name.lower() == filename:
                    print(os.path.join(root, name))


    @handle_exceptions
    def find_type(self, path:str, fileType:str) -> None:
        """
        Find file or directory by type and name.
        """

        if fileType not in ("f", "d"):
            raise ValueError("Type must be 'f' or 'd'")


        for root, dirs, files in os.walk(path):
            if fileType == "f":
                for name in files:
                    print(os.path.join(root, name))
            
            elif fileType == "d":
                for d in dirs:
                    print(os.path.join(root, d))

    @handle_exceptions
    def find_size(self, path:str, size:str, fileType:str = "f") -> None:
        """
        Find files larger than given size in MB.
        """

        if fileType != "f":
            raise ValueError("Size works only for files")

        if not size.lower().endswith("m"):
            raise ValueError("Only Mb unit is supported")

        # Detect operator
        if size.startswith("+"):
            operator = ">"
            value = size[1:-1]
        elif size.startswith("-"):
            operator = "<"
            value = size[1:-1]
        else:
            operator = "="
            value = size[:-1]

        if not value.isdigit():
            raise ValueError("Invalid size value")

        size_mb = int(value)
        size_bytes = size_mb * 1024 * 1024

        for root, _, files in os.walk(path):
            for name in files:
                full_path = os.path.join(root, name)
                try:
                    file_size = os.path.getsize(full_path)

                    if (
                        (operator == ">" and file_size > size_bytes) or
                        (operator == "<" and file_size < size_bytes) or
                        (operator == "=" and file_size == size_bytes)
                    ):
                        print(full_path)

                except PermissionError:
                    continue
                    

    @handle_exceptions
    def find_user(self, path:str, username:str, fileType:Optional[str] = None) -> None:
        """
        Find files owned by a specific user.
        """
        
        for root, dirs, files in os.walk(path):
            target = []

            if fileType == "f":
                target = files
            elif fileType == "d":
                target = dirs
            else:
                target = files + dirs

            for name in target:
                full_path = os.path.join(root, name)
                try:
                    owner = self.get_owner_windows(full_path)

                    if owner and owner.lower() == username.lower():
                        print(f"{full_path} -> {owner}")
                except PermissionError:
                    continue
               

    @handle_exceptions
    def find_empty(self, path:str, fileType: Optional[str] = None) -> None:
        """
        Find empty files or directories""
        """

        for root, dirs, files in os.walk(path):
            if fileType == "f":
                for name in files:
                    fullPath = os.path.join(root, name)
                    try:
                        if os.path.getsize(fullPath) == 0:
                            print(fullPath)
                    except PermissionError:
                        continue
            elif fileType == "d":   
                if not dirs and not files:
                    print(root)

# Creating object
findCommand = findCommand()


@handle_exceptions
def run_command(command):

    split = command.split()
    if not split:
        raise ValueError("Empty commands")

    if split[0] != "find":
        raise ValueError("Invalid command, use find only.")

    if len(split) < 3:
        raise ValueError("Invalid find syntax")

    path = split[1]
    validate_path(path)

    if "-name" in split:
        index = split.index("-name")
        findCommand.require_argument(split, index, "-name")
        filename = split[index + 1].strip('"').strip("'")
        fileType = split[split.index("-type") + 1] if "-type" in split else None
        findCommand.find_name(path, filename, fileType)


    elif "-iname" in split:
        index = split.index("-iname") 
        findCommand.require_argument(split, index, "-iname")
        filename = split[index + 1]
        fileType = split[split.index("-type") + 1] if "-type" in split else None
        findCommand.find_iname(path, filename, fileType)

    
    elif "-empty" in split:
        fileType = split[split.index("-type") + 1] if "-type" in split else None
        findCommand.find_empty(path, fileType)

    elif "-user" in split:
        userIndex = split.index("-user")
        findCommand.require_argument(split, userIndex, "-user")
        username = split[userIndex + 1]
        fileType = split[split.index("-type") + 1] if "-type" in split else None
        findCommand.find_user(path, username, fileType)

    elif "-type" in split and "-name" not in split:
        index = split.index("-type")
        findCommand.require_argument(split, index, "-type")
        fileType = split[index + 1]
        findCommand.find_type(path, fileType)

    elif "-size" in split:
        sizeIndex = split.index("-size")
        findCommand.require_argument(split, sizeIndex, "-size")
        size = split[sizeIndex + 1]
        fileType = split[split.index("-type") + 1] if "-type" in split else "f"
        findCommand.find_size(path, size, fileType)

    else:
        raise ValueError("Not supported find options.")


while True:

        # Getting user input
        command = input("skumarvel-SUBHA$ ").strip()

        if command == "exit":
            break
        else:
            run_command(command)

