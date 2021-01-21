a = ["Apple", "Orange", "Banana", "Jackfruit", "Bredfruit"]
a[2] = 'Nothing'
print(a, end="\n")

b = ["Apple", "Orange", "Nothing", "Jackfruit", "Bredfruit"]
print(end="\n")
print("Length of b : ", len(b), end="\n\n")
b.insert(2, "Banana")
print(b)
print("Length of b After insert : ", len(b), end="\n\n")
