ice = int(input('Введите количество упаковок мороженого: '))
people = 2
for i in range(ice + 1, 2, -1):
    if ice % i == 0:
        people = i
print(people)