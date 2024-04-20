count = 0

while True:
    k = int(input('Введите количество веревок(или 0 для окончания): '))
    if k == 0:
        break
    if k % 4 == 0:
        count += 1

print(count)