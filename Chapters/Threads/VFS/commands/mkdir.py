from nodes.node import Node

class MkdirCommand:
    def run(self, fileresolve, arguments):
        """
        Creating directory
        """
        # Slicing to get directory name
        names = [arg for arg in arguments if not arg.startswith("-")]
    
        for name in names:
            if name in fileresolve.current_working_dir.children:
                raise Exception(f"{name} already exist")

        # Creating child node for the given parent
            fileresolve.current_working_dir.children[name] = Node(name, "dir", fileresolve.current_working_dir)  

