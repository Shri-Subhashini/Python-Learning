from nodes.node import Node

class CatCommand:
    """
    Cat command class
    """
    def run(self, fileresolve, arguments):

        if not arguments:
            raise Exception("Missing arguments")
        
        current_working_dir = fileresolve.current_working_dir

        #cat > filename
        if arguments[0] == ">":
            name = arguments[1]
            node = Node(name, "file", current_working_dir)
            node.content = input("Enter content: ")
            current_working_dir.children[name] = node

        # cat >> filename
        elif arguments[0] == ">>":
            name = arguments[1]
            if name not in current_working_dir.children:
                raise Exception("File not found")
            current_working_dir.children[name].content += input("Append content: ")

        # cat filename
        else:
            node = fileresolve.path_set(arguments[0])
            if not node.is_file():
                raise Exception("Not a file")
            print(node.content)