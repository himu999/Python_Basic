row = int(input("Enter the row number : "))
for i in range(0, row):
    for j in range(0, row-i-1):
        print(end=" ")
    for k in range(0, i+1):
        print("*", end="")
    print()
