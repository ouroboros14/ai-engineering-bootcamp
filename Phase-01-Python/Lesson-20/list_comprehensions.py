numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number**2 for number in numbers]
print(squares)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

even_squares = [number**2 for number in numbers if number % 2 == 0]
print(even_squares)

words = ["Python", "AI", "Machine", "Learning", "Data"]

word_lengths = [len(word) for word in words]
print(word_lengths)

filtered_words = [word for word in words if len(word) > 4]
print(filtered_words)

numbers = [1, 2, 3, 4, 5]

labels = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(labels)

# The difference between list comprehensions and traditional loops is that list comprehensions provide a more concise and readable way to create lists.
# They allow you to generate a new list by applying an expression to each item in an existing iterable, optionally filtering items based on a condition.
# Traditional loops, on the other hand, require more lines of code and can be less intuitive, especially for simple transformations or filtering operations.