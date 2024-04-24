numbers = [1, 2, 3, 4, 5, 6]
square_numbers = map(lambda x: x ** 2, numbers)
print(list(square_numbers))

print(' ')
store = [
    ('Apple Juice', 3.99),
    ('Milkshake', 2.99),
    ('Meat-Pie', 5.99),
    ('Samoosa', 1.99),
]

cost_Euro = lambda data: (data[0], data[1] * 0.82)
store_euro = list(map(cost_Euro, store))
for i in store_euro:
    print(i)
