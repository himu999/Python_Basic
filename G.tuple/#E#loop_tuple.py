tup = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
tup1 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

print("Element of tuple : ", end=" ")
for i in tup:
    print(i, end=" ")
print()

k = 0
print("Element of tuple1 : ", end=" ")
while k < len(tup1):
    print(tup1[k], end=" ")
    k = k+1
print()
