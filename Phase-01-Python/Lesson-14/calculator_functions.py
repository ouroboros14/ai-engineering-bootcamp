def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    print(a / b)

add(6, 7)
add(6, 9)
add(4, 20)

print()
subtract(10, 5)
subtract(20, 10)
subtract(100, 50)

print()
multiply(5, 5)
multiply(10, 10)
multiply(6, 7)

print()
divide(10, 2)
divide(20, 0) # This will give a ZeroDivisionError.
divide(3, 1)

def greet(name):
    print(f"Hello, {name}!")

greet("Vrushabh")
greet("OpenAI")
greet("Future AI Engineer")