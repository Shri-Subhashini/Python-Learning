#Exception handler

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("OOPS! That was not a valid number. Try again")
    except (TypeError, ZeroDivisionError):
        print("Exception Occurs")

#Exception Example - first except block already handled the exception raised in the try block, and exceptions raised within a handler are not passed back to the same try block or to other handlers in the same try-except statement.
try:
    print("Trying something risky.")
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")
  #  y = 10 / 0  # This will raise another ZeroDivisionError inside the handler
except Exception:
    print("Caught a general Exception!")


# Class Exceptions

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B,C,D]:
    try:
        raise cls()
    # except B:
    #     print("B")
    except C:
        print("C")
    except D:
        print("D")
    # except C:
    #     print("C")
    except B:
        print("B")

#Exception Example
# The __str__() method is defined for most exceptions and is used to provide a string representation of the exception.

try:
    raise Exception('hi', 'hello')
except Exception as exp:
    print(type(exp))
    print(exp.args)
    print(exp) # Prints readable string format of that exception by using __str__() method which was called automatically (exp.__str__())
    a,b = exp.args
    print("a: ", a)
    print("b: ", b)

# Re-raising Exception

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")  
        raise  # Re-raise the exception to propagate it further

def main():
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Handling error in main: {e}")  # Handle it at a higher level

main()

'''
Explanation:

divide function

The divide function tries to perform division (a / b).
If a ZeroDivisionError occurs (i.e., dividing by zero), it is caught by the except block.
The exception is logged or printed (e.g., print(f"Error: {e}")).
Then, the exception is re-raised using raise. This allows the calling function (in this case, main()) to handle the exception as well.

main function

The main() function calls divide(10, 0), which triggers the ZeroDivisionError.
The exception is propagated from the divide function and is caught by the except block in main().
The exception is then handled by printing a message: print(f"Handling error in main: {e}").

'''

#Re-rasising

import sys
try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS Error: ", err)
except ValueError:
    print("Cold not change data to integer")
except Exception as err:
    print(f"Unexpected Error {err= }, {type(err)=}")
    raise
'''
# Passing args and checking using try except

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('Cannot open ', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()   # Run using: python Chapter8.py file1.txt file2.txt
# Output:
# file1.txt has 2 lines
# file2.txt has 2 lines

'''

# Exeption using function call in try
def hi():
    x = 12/0
try:
    hi()
except ZeroDivisionError as err:
    print("Handling run-time error: ", err)


# Raising Exception

'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

'''

#Exception Chaining

'''
try:
    open("database.sqlite")
except:
    raise RuntimeError("unable to handle error")


o/p
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Python-Learning\Python-Learning\Chapters\Chapter8.py", line 149, in <module>     
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error


def greet():
    raise ConnectionError
try:
    greet()
except ConnectionError as conn:
    raise RuntimeError("Failed") from conn


Output for from conn
Traceback (most recent call last):
  File "D:\Python-Learning\Python-Learning\Chapters\Chapter8.py", line 170, in <module>     
    greet()
    ~~~~~^^
  File "D:\Python-Learning\Python-Learning\Chapters\Chapter8.py", line 168, in greet        
    raise ConnectionError
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\Python-Learning\Python-Learning\Chapters\Chapter8.py", line 172, in <module>     
    raise RuntimeError("Failed") from conn    
RuntimeError: Failed


Output for None:
Traceback (most recent call last):
  File "D:\Python-Learning\Python-Learning\Chapters\Chapter8.py", line 172, in <module>     
    raise RuntimeError("Failed") from None    
RuntimeError: Failed
'''
#Defining cleanup actions
'''
try:
    raise KeyboardInterrupt
finally:
    print('Bye')

o/p
Bye
Traceback (most recent call last):
  File "D:\Python-Learning\Python-Learning\Chapters\Chapter8.py", line 199, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
'''
def test():
    try:
        return "From try"
    finally:
        print("In finally")

print(test())

#Predefined clean up actions

with open("file1.txt") as f:
    for line in f:
        print(line, end = "")

# Raising and Handling Multiple Unrelated Exceptions

def f():
    # excs = [OSError('error 1'), SystemError('error 2')]
    # raise ExceptionGroup('there was a problem', excs)
    raise ExceptionGroup(
        "group1", [OSError(1), SystemError(2), ExceptionGroup("group 2", [OSError(3), RecursionError(4)])])

try:
    f()
# except Exception as e:
#     print(f"caught{type(e)}: e")

except* OSError as e:
    print("OsError occured")
except* SystemError as e:
    print("SystemError occured")
except* RecursionError as e:
    print("There were RecursionErrors")

#Handled recursionexception also, so there is no traceback and no re-raise

'''
try:
    raise TypeError('bad type')
except Exception as exe:
    exe.add_note('Exception handled note')
    raise
except ValueError as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

'''