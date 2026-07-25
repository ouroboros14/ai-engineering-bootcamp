def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

divide(10, 2)
divide(20, 0)
divide(50, 5)

student = {
    "name": "Vrushabh",
    "course": "AI Engineering"
}

try:
    print(student["cgpa"])
except KeyError:
    print("Error: CGPA not found.")

def greet(name):
    try:
        print(f"Hello, {name}!")
    finally:
        print("Greeting completed.")

greet("Vrushabh")
greet("OpenAI")

# We should use specific exception handling to catch only the exceptions we expect, rather than using a general exception handler.