language = "Python"

def show_language():
    print(f"The programming language is {language}.")

show_language()
print(f"This is a practice of variable scope in {language}.")

def introduce():
    name = "Vrushabh"
    print(f"My name is {name}.")

introduce()
# print(f"Outside the function, the name variable is not accessible: {name}.")  # This will raise an error because 'name' is not defined in this scope.

count = 10
def increment():
    global count
    count += 5

increment()
increment()
print(f"The value of count after incrementing is {count}.")

# Developers generally avoid using global variables as they can lead to code that is difficult to understand and maintain.