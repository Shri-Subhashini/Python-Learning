from time import sleep
from threading import *
from concurrent.futures import ThreadPoolExecutor


# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)


# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)


# t1 = Hello()
# t2 = Hi()

# t1.start()
# sleep(0.2)
# t2.start()

# t1.join()
# t2.join()

# print("Bye")


import threading
import time

stop_event = threading.Event()


def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
print(threading.current_thread().name)
t2.start()
print(threading.current_thread().name)

print(t1.is_alive())
t1.join()
# stop_event.set()
print("Stopped t1")
print(t1.is_alive())
t2.join()




# print(threading.current_thread().name)

with ThreadPoolExecutor(max_workers = 1) as exec:
    future = exec.submit(task, "A")
    print(future.result())

print("Main thread completed")

# print(threading.enumerate())
for t in threading.enumerate():
    print(t.name)
    print(t.ident)

print(f"Current Thread: {threading.current_thread().name}")

from concurrent.futures import ThreadPoolExecutor
from time import sleep

values = [3,4,5,6]

def cube(x):
    return x*x*x
    

if __name__ == '__main__':
    result =[]
    with ThreadPoolExecutor(max_workers=5) as exe:
        f = exe.submit(cube,2)
        print(f.result())
        # Maps the method 'cube' with a list of values.
        result = exe.map(cube,values)
    
    for r in result:
      print(r)