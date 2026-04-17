# n = 10

# try:
#     res = n /0
# except ZeroDivisionError:
#     print("Can't divide by 0")

# try:
#     x = int("str")
#     inv = 1 / x
# except ValueError:
#     print("Not valid")
# except ZeroDivisionError:
#     print("Zero has no inverse")

# a = ["10", "twenty", 30]
# try:
#     total = int(a[0]) + int(a[1])

# except (ValueError, TypeError) as e:
#     print("Error ", e)

# except IndexError:
#     print("iNDEX OUT OF RANGE")


# try:
#     x = int("10")
# except ValueError:
#     print("Error occured")
# else:
#     print("No error")
# finally:
#     print("Program finished")

# try:
#     age = -5
#     if age < 0:
#         raise ValueError("Age cannot be negative")

# except ValueError as e:
#     print("Error: ", e)


# class AgeError(Exception):
#     pass

# def set(age):
#     if age < 0:
#         raise AgeError("Age cannot be negative.")
#     print(f"Age set to {age}")

# try:
#     set(-5)
# except AgeError as e:
#     print(e)



