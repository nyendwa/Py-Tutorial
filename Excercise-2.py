# Nested loop : is a concept of having a loop inside another
rows = int(input('How many rows '))
columns = int(input('How many columns '))
symbol = input('Select a symbol ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()
    