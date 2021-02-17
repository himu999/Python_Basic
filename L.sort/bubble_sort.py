a = []
b = int(input("How many element you want to store in list : "))
for j in range(b):
    value = int(input())
    a.append(value)

for i in range(0, len(a)-1):

    if a[i] > a[i+1]:

        while i != -1:

            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
            i = i - 1

print(a)



