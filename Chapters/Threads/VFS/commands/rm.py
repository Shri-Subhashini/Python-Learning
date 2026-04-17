
# To delete recursively
def delete_recursive(node):
    if node.is_directory():
        for child in list((node.children.values())): #Converting as list becoz dict cannot be modified while iterating
            delete_recursive(child)
    del node.parent.children[node.name]


class RmCommand:
    """
    Rm class Command - Remove files and folders
    """

    def run(self, fileresolve, arguments):
        is_recursive = "-r" in arguments or "-rf" in arguments
        name = arguments[-1]
        node = fileresolve.path_set(name)
        if node.is_directory() and not is_recursive:
            raise Exception(name)
        
        # rm -r filename / rm -rf filename
        if is_recursive:
            delete_recursive(node)
        # rm filename
        else:
            del node.parent.children[node.name]


        
