
class CdCommand:
    """
    Cd command Class
    """

    def run(self, fileresolve, arguments):
        options = arguments[0] if arguments else "~"
        fileresolve.prev_working_dir = fileresolve.current_working_dir
        # cd -
        if options == "-":
            if fileresolve.prev_working_dir:
                fileresolve.current_working_dir, fileresolve.prev_working_dir = fileresolve.prev_working_dir, fileresolve.current_working_dir
            return
        #  cd ~
        if options == "~":
            fileresolve.current_working_dir = fileresolve.root
        # cd pathname, cd ., cd.., cd /
        else:
            fileresolve.current_working_dir = fileresolve.path_set(options)