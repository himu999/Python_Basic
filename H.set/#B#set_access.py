a = {"first", 2, "second", "0", "+"}
print(a)
b = list(a)
print(b)

for i in a:
    print(i, end="\t")

print(end="\n\n")
print("first" in a)
print(b)
print(b.index(2))