age = int(input("Enter your age: "))

if age <= 12:
    print("Hi kiddo! You are a child.")
elif age <= 17:
    print("Hey teen! You are a teenager.")
elif age <= 59:
    print("Hello adult! You are an adult.")
else:
    print("Good evening senior! You are a senior citizen.")