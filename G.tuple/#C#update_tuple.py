a = ("a", "b", "c", "d", "e")
b = list(a)
b.append("f")
a = tuple(b)

print(type(a))

print(a)

"""
Tuple is unchangeable but list is changeable that's why we need to convert tuple to list
Thank you
"""

c = list(a)
c.remove("f")
a = tuple(c)
print(a)
