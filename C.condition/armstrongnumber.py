"""
    To check a number is armstrong or not?
    153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3
    1544 = 1 ^ 4 + 5 ^ 4 + 4 ^ 4 + 4 ^ 4
"""
num = input("Enter the number : ")
digit = int(num)
temp = digit
power = len(num)
summation = 0

while digit != 0:
    digit_mod = digit % 10
    digit = digit // 10
    summation = summation + pow(digit_mod, power)
if summation == temp:
    print(num, " : is a armstrong number")
else:
    print(num, " : is not a armstrong number")
