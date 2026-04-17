from nodes.node import Node

class RmdirCommand:
    """
    To remove folder
    """
    
    def run(self, fileresolve, arguments):
        remove_parents = "-p" in arguments
        names = [arg for arg in arguments if not arg.startswith("-")]
        for path in names:
            node = fileresolve.path_set(path)
            self.remove_directory(node, remove_parents)

    def remove_directory(self, node, remove_parents):        
        if not node.is_directory():
            raise Exception("Not a directory")
        
        if node.children:
            raise Exception("Directory not empty")
        
        # rmdir foldername
        parent = node.parent
        del parent.children[node.name]

        # rmdir -p /home/user
        if remove_parents:
            self.remove_parent_dir(parent)
        
    def remove_parent_dir(self, node):
        """
        To remove parent folder - rmdir -p /home/user
        """
        while node.parent and not node.children:
            parent = node.parent
            del parent.children[node.name]
            node = parent

