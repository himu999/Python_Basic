f = open("some.txt", "r")
print()
# t = f.read()
# print(t)
# print(f.readline(), end="")
# print(f.readline(), end="")
# print(f.readlines())

print(f.read())
f.close()

f = open("some.txt", "r")
print(f.readlines())

f.close()

k = open("img.jpg", "br")
print(k.read())

k.close()
