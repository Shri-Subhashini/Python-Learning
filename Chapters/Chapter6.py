from fibo import fib as fibonacci, fib2 as fibonacci2

import builtins
import sys
# To reload the modules automatically without restarting the interpreter again, when we change in the particular module.

# import importlib
# importlib.reload(module_name)


# Import variants

# import fibo => fibo.fib(500) - crt
# from fibo import fib, fib2  => fib(500) - crt; fibo.fib(500) don't use - error becz name fibo is nt introduced in that module.
# from fibo import * => fib(500) crt
# import fibo as fib - alias => fib.fib(500) - crt
# from fibo import fib as finonacci => fibonacci(300) - crt

# Thsese for import fibo 

# fibo.fib(200) 
# fibo.fib2(300)
# print("Module Name: ", fibo.__name__)


# These for from fibo import fib as fibonacci, fib2 as fibonacci2

fibonacci(200)   # modname.itemname. (to use module's global variables)
print("Fibonacci series from fib2 : ",fibonacci2(2000))
print("Module Name: ", __name__) # Module Name:  __main__

# If you run a Python file directly (i.e., you execute python script.py), Python sets __name__ to __main__. This indicates that the file is being executed as the main program, not as an imported module.
# If you import the file as a module, __name__ is set to the name of the module (e.g., 'fibo' if you import fibo.py).

print("Built in Names :", sys.builtin_module_names)

a = [1,2,3,4,5]

dir(sys)
# print("########")
#dir()
dir(builtins)

