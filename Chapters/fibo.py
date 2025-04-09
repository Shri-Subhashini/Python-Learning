#Fibonacci module

def fib(n):    
    a, b = 0, 1
    while a < n:
        print("From Fibo Module: ", a)
        a, b = b, a+b
    print("####s")

def fib2(n):  
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
def greet():
    print("Hi")
    
# To make this module as executable Script

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    greet()
    # fibo(200)
