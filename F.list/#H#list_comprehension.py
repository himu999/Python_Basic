a = ["apple", "kiwi", "cherry", "banana", "mango"]
b = []
c = []

for x in a:
    if "a" in x:
        b.append(x)
    else:
        c.append(x)

print("Element of list a : ", a)
print("Element of list b : ", b)
print("Element of list c : ", c)

# With short hand
k = [x for x in a if "a" in x]
print("Element of list k : ", k)
l = [x for x in a if x != "apple"]
print("Element of list l : ", l)
