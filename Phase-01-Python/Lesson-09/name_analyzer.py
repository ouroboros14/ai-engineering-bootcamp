user_name = input("Enter your name: ")

print(f"Hello, {user_name}!")
print(f"Your name has {len(user_name)} characters.")
print(f"First character: {user_name[0]}")
print(f"Last character: {user_name[-1]}")

print("\n")
for character in user_name:
    print(character)

manual_count = 0
for character in user_name:
    manual_count += 1
print(f"\nTotal characters counted using loop: {manual_count}")
if len(user_name) == manual_count:
    print("The manual count matches len()!")
else:
    print("Something went wrong.")

# user_name[0] = 'X'  # This will raise an error because strings are immutable in Python.

print("\n")
for reverse_character in reversed(user_name):
    print(reverse_character)