def oddeven(a):
    if a % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"


n = int(input("Enter your number : "))
k = oddeven(n)
print(k)
