
students = [
    ("Ram", 72),
    ("shyam", 83),
    ("Gyan", 82)
]
# print(students)


def sort_students(stu):
    return stu[1]


# students.sort(key=lambda parameter:statement)

students.sort(key=lambda stu: stu[1])

print(students)
