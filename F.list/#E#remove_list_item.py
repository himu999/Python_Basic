a = ["Nothing", 'Apple', 'Orange', 'Banana', 'Jackfruit', 'Bredfruit', 'cherry', 'mango', 'pineapple', 'papaya']

print(a)
print("length of a : ", len(a))
a.remove("Nothing")

print(a)
print("length of a : ", len(a))
a.pop(2)
print(a)
print("length of a : ", len(a))
a.pop()
print(a)
print("length of a : ", len(a))

del a[-4]
print(a)
print("length of a : ", len(a))

"""
 for complete list delete we can use del. for example del list name
"""
