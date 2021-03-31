num = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if num <= 0:
    print("Enter a positive integer")
elif num == 1:
    print(n1)
else:

    while count <= num:
        summ = n1 + n2
        n1 = n2
        n2 = summ
        count += 1

print("fibonacci number for", count-1,"is", n1)
