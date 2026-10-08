student = {
    "name": "Vrushabh",
    "age": 20,
    "course": "AI Engineering",
    "cgpa": 9.5
}

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key}: {value}")

for student in student.items():
    print(student)

student.get("name")
student.get("university")
student.get("university", "Not provided")

student.update({"age": 21, "university": "Ajeenkya D Y Patil University", "country": "India"})
print(student)

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2 for number in numbers
}
print(squares)

prediction = {
    "label": "cat",
    "confidence": 0.94,
    "model": "ImageClassifier"
}

for key, value in prediction.items():
    print(f"{key}: {value}")

# .get() is safer than using dictionary[key] because it won't raise a KeyError if the key doesn't exist. Instead, it will return None or a default value if provided.