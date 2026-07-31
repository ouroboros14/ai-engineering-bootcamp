fruits = ["Apple", "Banana", "Orange"]

fruits.append("Mango")

fruits.insert(1, "Grapes")

fruits.remove("Orange")

removed_fruit = fruits.pop()

print(fruits)
print(f"Removed fruit: {removed_fruit}")

marks = [78, 85, 92, 67, 88]

print(len(marks))

print(f"First mark: {marks[0]}")

print(f"Last mark: {marks[-1]}")

languages = ["Python", "C#", "Java", "JavaScript"]

print("Python" in languages)
print("Go" in languages)

for fruit in fruits:
    print(fruit)

# Use pop() when you need to remove an item and also use the removed value later. Use remove() when you simply want to remove a specific value from the list.