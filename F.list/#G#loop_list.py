a = ["a", "b", "c", "d", "e"]

for x in a:
    print(x, end=" ")
print(end="\n")

for i in range(len(a)):
    print(a[i], end=" ")

# Using a While Loop
print(end="\n")
i = 0
while i < len(a):
    print(a[i], end=" ")
    i = i+1

print(end="\n")

# Shorthand
[print(i, end=" ") for i in a]
