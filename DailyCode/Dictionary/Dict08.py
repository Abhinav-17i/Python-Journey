student = {
    "John": 85,
    "Alice": 90,
    "Bob": 78
}

name = input("Enter student name: ")

if name in student:
    print("Marks:", student[name])
else:
    print("Student not found")