a = {"name": "akash", "job": "farmer", "class": "classless"}

for x in a:
    print(a[x], end=" ")

print()

for x in a.keys():

    print("All keys of a dictionaries : ", x, end="")

print()
for y in a.values():
    print("All values of a dictionaries : ", y, end=" ")
print(end="\n\n")
for x, y in a.items():
    print(x, ":", y)
