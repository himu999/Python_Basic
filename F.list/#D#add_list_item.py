a = ["Apple", "Orange", "Banana", "Jackfruit", "Bredfruit"]

a.append("cherry")
a.insert(0, "Nothing")
print(a)
b = ["mango", "pineapple", "papaya"]
a.extend(b)
"""
 Extend just merge two list
"""
print(a)
print(b)
b.extend(a)
print(b)
