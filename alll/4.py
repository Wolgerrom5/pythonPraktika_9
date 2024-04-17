count = 0

K = int(input("Введите количество веревок: "))

while K != 0:
    if K % 3 == 0:
        count += 1
    K = int(input("Введите количество веревок: "))

print(count)
