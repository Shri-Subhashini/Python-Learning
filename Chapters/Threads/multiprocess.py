import multiprocessing
import os

# 1

def cube(num):
    print(num*num*num)

def square(num):
    print(num*num)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = cube, args = (10,))
    p2 = multiprocessing.Process(target = square, args = (10,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Completed")


# 2

def worker1():
    print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
    print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
    print("ID of main process: {}".format(os.getpid()))
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)
    p1.start()
    p2.start()
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))
    p1.join()
    p2.join()
    print("Both processes finished execution!")
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))



# 3

result = []
def square(myList):
    global result
    for num in myList:
        result.append(num * num)

    print(f"Result in process 1 {result}")

if __name__ == "__main__":
    myList = [1,2,3,4]
    p1 = multiprocessing.Process(target = square, args = (myList,))
    p1.start()
    p1.join()

    print(f"Result in main program {result}")
    