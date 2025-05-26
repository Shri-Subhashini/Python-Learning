import pendulum
from .hello import say_hello

now = pendulum.now()
print("Current time:", now.to_datetime_string())

print(say_hello())
