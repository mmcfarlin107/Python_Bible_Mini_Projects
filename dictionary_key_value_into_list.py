# for loop practice script to push dictionary values into a new list

students = {
    'male': ['doug', 'brad', 'kenny', 'smith'],
    'female': ['jessi', 'kathy', 'michelle', 'kelly']
}

student_names_with_a = []
for student in students.keys():
    for name in students[student]:
        if "a" in name:
            student_names_with_a.append(name)

print(student_names_with_a)