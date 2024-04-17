import math

number = float(input('Введите число больше 2 : '))
while number >= 2:
    number = math.sqrt(number)
print("{:.3f}".format(number))
