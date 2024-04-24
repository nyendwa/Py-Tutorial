friends = {
    ('Lois', 19),
    ('Meg', 14),
    ('Pam', 15),
    ('Wanzi', 21),
    ('Jay', 22),
    ('Chris', 18),
}

age = lambda data: data[1] >= 18
legal_age = list(filter(age, friends))
for i in legal_age:
    print(i)
