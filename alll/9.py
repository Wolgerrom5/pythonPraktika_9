N = int(input("Введите наибольшее количество точек на одной плитке кости домино (K): "))

dominoes= 0
for i in range(N + 1):
    for j in range(i, N + 1):  # Чтобы не учитывать дублирующие комбинации
        dominoes += i + j

print(dominoes)
