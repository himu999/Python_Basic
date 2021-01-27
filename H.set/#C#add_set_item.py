a = {22, "Himu", "Maa", "Baba", "Vai", "Bon"}
print("Element of a : ", a)
print(list(a).index(22))
a.add("Family")
print(a)
b = {"Fruits", "Cherry", "Banana", "Guava", "Jackfruit", "Mango", "Lychee"}
print("Element of b : ", b)
# Merge two set a and b

b.update(a)


print(b)

# Merge list with set
c = ["Mind", "Strong", "Love", "No hate"]
a.update(c)
print(a)
