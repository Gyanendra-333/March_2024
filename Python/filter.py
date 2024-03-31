
students = [
    ("Ram", 72),
    ("shyam", 83),
    ("Gyan", 82)
]

new_list = list(filter(lambda x: x[1] < 90, students))

print(new_list)
