def palindrome(num):
    return str(num) == str(num)[::-1]


i = 1
while not (palindrome(i % 100000) and palindrome(i // 10 % 100000) and palindrome(i // 1000)):
    i += 1

print(i)
