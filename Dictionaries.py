capital = {'Zambia': 'Lusaka',
           'China': 'Beijing',
           'Russia': 'Moscow',
           'UK': 'London'
           }

# print(capital.get('Russia'))
print(capital.items())
print(capital.values())
for key, value in capital.items():
    print(key, value)
