student = {
    "name": "Vrushabh",
    "age": 20,
    "course": "AI Engineering",
    "cgpa": 9.5
}

print(f"The entire dictionary: {student}")
print(f"The student's name is {student["name"]} and their CGPA is {student["cgpa"]}.")

student["cgpa"] = 9.75

student["skills"] = ["Python", "Machine Learning", "Data Analysis"]

print(f"The updated dictionary: {student}")

print(f"Accessing internship in the dictionary: {student["internship"]}")  # This will raise a KeyError since "internship" key does not exist.

# A dictionary can be used instead of a list when you want to store data in key-value pairs, allowing for more descriptive and organized data representation.