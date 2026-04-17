import fnmatch
from nodes.fileResolve import FileResolve


class FindCommand:
    """
    Find class command - to find files based on options
    """

    def run(self, fileresolve, arguments):
        if not arguments:
            raise ValueError("Missing path")

        start = arguments[0]
        options = arguments[1:]

        node = fileresolve.path_set(start)

        def match_options(options):
            matches = {
                "name" : None,
                "iname" : None,
                "type" : None,
                "size" : None,
                "user" : None
            }

            index = 0

            # options mapping
            while index < len(options):
                opt = options[index]

                if opt == "-name":
                    matches["name"] = options[index+1].strip('"').strip("'")
                    index += 2
                
                elif opt == "-iname":
                    matches["iname"] = options[index + 1].strip('"').strip("'")
                    index += 2

                elif opt == "-type":
                    matches["type"] = options[index + 1]
                    index += 2
                elif opt == "-size":
                    matches["size"] = options[index + 1]
                    index += 2
                elif opt == "-user":
                    matches["user"] = options[index + 1]
                    index += 2
                else:
                    raise ValueError(f"Invalid option")

            return matches


        matches = match_options(options)


        def match_size(node, size):
            """
            To claculate size - find . -size +1M
            """
            size_in_bytes = node.size()

            if not size.lower().endswith("m"):
                raise ValueError("Size supports only MB")
            
            if size.startswith("+"):
                range = int(size[1:-1]) * 1024 * 1024
                return size_in_bytes > range
            
            elif size.startswith("-"):
                range = int(size[1:-1]) * 1024 * 1024
                return size_in_bytes < range
            
            else:
                range = int(size[1:-1]) * 1024 * 1024
                return size_in_bytes == range

       
        def mapping(node):
            
            # find . -name filename
            if matches["name"]:
                if not fnmatch.fnmatch(node.name, matches["name"]):
                    return False

            # find . -iname filename
            if matches["iname"]:
                if node.name.lower() != matches["iname"]:
                    return False
            # find . -type f/d filename
            if matches["type"]:
                if matches["type"] == "f" and not node.is_file():
                    return False
                if matches["type"] == "d" and not node.is_directory():
                    return False
                
            # find . -size +1M
            if matches["size"]:
                if not node.is_file():
                    return False
                if not match_size(node, matches["size"]):
                    return False
            
            if matches["user"]:
                if node.owner != matches["user"]:
                    return False

            return True

        def full_path(node):
            """
            To print full path
            """

            parts = []
            while node.parent:
                parts.append(node.name)
                node = node.parent
            return "/" + "/".join(reversed(parts))

        
        def traverse(node):
            """
            Dept first Search
            """
            
            if mapping(node):
                print(full_path(node))

            if node.is_directory():
                for child in node.children.values():
                    traverse(child)

        traverse(node)

        

        