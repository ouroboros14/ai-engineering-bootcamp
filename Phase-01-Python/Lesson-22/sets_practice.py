prog_languages = ["Python", "Java", "C++", "Java", "Ruby", "C++", "C#"]
set_prog_languages = set(prog_languages)

print(prog_languages)
print(set_prog_languages)

print(len(prog_languages))
print(len(set_prog_languages))
# Length of the original list is 7, while the length of the set is 5, indicating that there are duplicate entries in the original list.

skills = {"Python", "SQL", "Git"}
skills.add("NumPy")
skills.update({"Pandas", "Scikit-learn"})
skills.remove("Git")
skills.discard("Java")

print(skills)
print(len(skills))

backend_skills = {"Python", "SQL", "Git", "Docker"}
ai_skills = {"Python", "NumPy", "Pandas", "SQL"}

unique_skills = backend_skills | ai_skills
common_skills = backend_skills & ai_skills
exclusive_backend_skills = backend_skills - ai_skills
exclusive_ai_skills = ai_skills - backend_skills
exactly_one_set = backend_skills ^ ai_skills

expected_labels = {"cat", "dog", "bird"}
predicted_labels = {"cat", "dog", "fish"}

print(expected_labels.issubset(predicted_labels))
print(expected_labels - predicted_labels)
print(predicted_labels - expected_labels)
print(expected_labels.issuperset(predicted_labels))

raw_emails = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
    "bob@example.com",
    "diana@example.com"
]

unique_emails = set(raw_emails)
print(len(raw_emails))
print(len(unique_emails))
print(len(unique_emails) - len(raw_emails))
print("alice@example.com" in unique_emails)
print("eve@example.com" in unique_emails)

sorted_emails = sorted(unique_emails)
print(sorted_emails)