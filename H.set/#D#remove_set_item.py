family = {"Maa", "Baba", "Bon", "Vai", "Happy", "Depression", "Critical time", "Beautiful"}

print(len(family))

print("Member of family : ", family)
family.remove("Depression")
print("Member of family : ", family)
family.discard("Critical time")
print("Element of family : ", family)

a = {22, "Life", "Strong", 99, "69"}
print("Element of a : ", a)
a.pop()
print("Element of a : ", a)
a.clear()
print(len(a))

del a
print("a deleted")
