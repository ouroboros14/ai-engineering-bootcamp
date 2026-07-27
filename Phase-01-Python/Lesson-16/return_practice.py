def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."

print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 5))

def square(number):
    return number ** 2

square(5)
square(10)
square(-4)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))
print(is_even(7))

# return is generally more useful than print because it allows the function to send data back to the caller, which can then be used in further calculations or logic.