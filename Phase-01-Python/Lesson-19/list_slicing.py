numbers = [10, 20, 30, 40, 50, 60, 70, 80]

first_three = numbers[:3]
print(first_three)

last_three = numbers[-3:]
print(last_three)

two_through_five = numbers[2:6]
print(two_through_five)

every_other = numbers[::2]
print(every_other)

reverse_numbers = numbers[::-1]
print(reverse_numbers)

students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

first_three_students = students[:3]
print(first_three_students)

last_two_students = students[-2:]
print(last_two_students)

every_other_student = students[::2]
print(every_other_student)

reverse_students = students[::-1]
print(reverse_students)

for index, student in enumerate(students):
    print(f"Index: {index}, Student: {student}")

numbers_task3 = [10, 20, 30, 40, 50]
selected = numbers_task3[1:4]

selected[0] = 999
print(f"Original list: {numbers_task3}")
print(f"Selected slice: {selected}")

# enumerate() function is used to get both the index and the value of each element in a list.