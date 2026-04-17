from nodes.node import Node

class LsCommand:
    """
    Ls command class - To list files and folders with metadata
    """

    def run(self, fileresolve, arguments): 

        options = {
            "show_hidden" : "-a" in arguments,
            "long_list" : "-l" in arguments or "-g" in arguments,
            "reverse" : "-r" in arguments,
            "recursive" : "-R" in arguments,
            "sort_time" : "-t" in arguments,
            "hide_owner" : "-g" in arguments,
            "list_dir" : "-d" in arguments

        }       
       
        node = fileresolve.current_working_dir

        # ls -d
        if options["list_dir"]:
            result = [node]
        # ls
        else:
            result = self.entries(list(node.children.values()), options)

        # ls -R

        if options["recursive"] and not options["list_dir"]:
            self.ls_recursive(node, result, options)
        
        else:
            self.print_details(result, options)
        
    def entries(self, result, options):

        # ls -a
        if not options["show_hidden"]:
            result = [res for res in result if not res.hidden]
        
        # ls -t
        if options["sort_time"]:
            result.sort(key = lambda x: x.modified_time)
        
        # ls -r
        if options["reverse"]:
            result.reverse()
        
        return result

    def ls_recursive(self, node, result, options):
        """
        To print recursive
        """

        print(f"\n{node.name}")

        self.print_details(result, options)

        for child in result:
            if child.is_directory():
                sub_child = self.entries(list(child.children.values()), options)
                self.ls_recursive(child, sub_child, options)

    
    def print_details(self, result, options):
        for res in result:
            if options["long_list"]:
                self.print_long_list(res, options["hide_owner"])
            else:
                print(res.name)

    # ls -l; ls -g
    def print_long_list(self, node, hide_owner):
        permission = node.mode
        size = node.size()
        modified_time = node.modified_time.strftime("%Y-%m-%d %H:%M")
        
        parts = [permission,]

        if not hide_owner:
            parts.append(node.owner)
        parts.append(node.group)

        parts.extend([str(size), modified_time, node.name])

        print(" ".join(parts))


       
        

            


            
    