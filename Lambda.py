students = [
    ('Joe', 'F', 47),
    ('Meg', 'A', 90),
    ('Lois', 'B', 60),
    ('Chris', 'C', 57),
    ('Govat', 'D', 30),
    ('Amanda', 'E', 35),
]
students.sort()
for student in students:
    print(student)

print(' ')
print('=======================')
grade = lambda grades: grades[2]
students.sort(key=grade, reverse=True)
for i in students:
    print(i)

print('=======================')

age = lambda ages: ages[1]
students.sort(key=age)
for j in students:
    print(j)
