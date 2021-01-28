a = {"a": "himel", "b": "hasan", 2: 5}
print(list(a.values())+list(a.keys()))

a[2] = "him"
print(a)
a.update({2: "himu"})

print(a)

'''b = []
c = [2, 3, 4]
c = c + b
print(c)
'''