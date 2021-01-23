a = ["a", "b", "c", "d"]
b = ["1", "2", "3"]
c = ["a", "b", "c", "d"]
d = ["1", "2", "3"]
e = ["a", "b", "c", "d"]
f = ["1", "2", "3"]
a = a+b
print("After extend , now element of a :", a)
c.extend(d)
print("After extend element of c : ", c)

for x in f:
    e.append(x)
print("After extend element of e : ", e)
