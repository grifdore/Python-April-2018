student_grades = {
    'bob': [2, 2],
    'petar': [5, 2, 5],
    'maria': [1, 6, 5, 6],
    'alex': [2, 2]
}
sorted_by_key = sorted(student_grades.items(), key=lambda kvp: (kvp[0], kvp[1]), reverse=True)
print(sorted_by_key)