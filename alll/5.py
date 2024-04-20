def is_palindrome(num):
    return str(num) == str(num)[::-1]


for i in range(100000, 999999):
    str_i = str(i)
    if is_palindrome(int(str_i[1:])) and is_palindrome(int(str_i[2:])) and is_palindrome(i):
        print(i)
        break
