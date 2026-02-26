marks = {
    "Math": 85,
    "Physics": 92,
    "Chemistry": 88,
    "English": 76
}

highest_mark = 0
highest_subject = ""

for subject in marks:
    if marks[subject] > highest_mark:
        highest_mark = marks[subject]
        highest_subject = subject

print("Marks:", marks)
print("Highest Scoring Subject:", highest_subject)
print("Highest Marks:", highest_mark)