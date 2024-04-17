N = int(input('Введите количество эскимо:'))
people = 1
while N % people != 0:
    people += 1
group = N // people
print(group)
