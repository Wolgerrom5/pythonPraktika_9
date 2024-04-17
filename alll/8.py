x = int(input("Введите число x: "))
count = 0

for i in range(1, int(x ** 0.5) + 1):
    for b in range(i, int(x ** 0.5) + 1):
        if i ** 2 + b ** 2 == x:
            count += 1

print(count)
