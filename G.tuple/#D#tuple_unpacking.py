a = ("a", "b", "c", "d", "e")
b = ("a", "b", "c", "d", "e")
c = ("a", "b", "c", "d", "e")
(f, g, h, i, j) = a
print(f, g)
(k, l, m, *n) = b
print(n)
(o, *p, q) = c
print(o)
print(p)
print(q)

