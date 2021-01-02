summation = 0
for i in range(1, int(input("Target value : "))+1):
    for j in range(1, i+1):
        summation = summation+j
print("Summation is : ", summation)

