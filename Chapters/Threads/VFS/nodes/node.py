from datetime import datetime

class Node:
    """
    Node class for initialization of Node
    """
    
    def __init__(self, name, node_type = "dir", parent = None):
        self.name = name
        self.type = node_type
        self.parent = parent
        self.children = {} if node_type == "dir" else None
        self.content = ""
        self.owner = "skumarvel"
        self.group = "user"
        self.hidden = name.startswith(".")
        self.created_time = datetime.now()
        self.modified_time = self.created_time

        if node_type == "dir":
            self.mode = "drwxr-xr-x"
        else:
            self.mode = "-rw-r--r--"

    def is_directory(self):
        return self.type == "dir"
    
    def is_file(self):
        return self.type == "file"
    
    def size(self):
        return len(self.content.encode()) if self.is_file() else 0

