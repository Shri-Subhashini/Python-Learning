from nodes.node import Node

class FileResolve:
    """
    Setting current_path and previous_path
    """
    def __init__(self):
        self.root = Node("/")
        self.current_working_dir = self.root
        self.prev_working_dir = None

    # To print current working directory
    def printWorkingDirectory(self):
        node = self.current_working_dir
        path = []
        while node.parent:
            path.append(node.name)
            node = node.parent
        return "/"+"/".join(reversed(path))

    # For root
    def path_set(self, path):
        if path == "/":
            return self.root
        
        # For Absolute path
        if path.startswith("/"):
            node = self.root
            parts = path.strip("/").split("/")
        
        # For Relative path
        else:
            node = self.current_working_dir
            parts = path.split("/")
        
        for part in parts:
            if part in ("", "."):
                continue

            if part == "..":
                node = node.parent or node
            elif node.is_directory() and part in node.children:
                node = node.children[part]
            else:
                raise FileNotFoundError(path)
        return node
