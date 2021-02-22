name = {
    "my": "Himu", "Her": "Rupa", "City": "Mars", "From": "Heaven"
}

print("Values of dictionary :", end=" ")

for i in name.values():
    print(i, end=", ")
print()
print("Keys of dictionary :", end=" ")
for j in name.keys():
    print(j, end=", ")
print("Items of dictionary :", end=" ")
for k in name.items():
    print(k, end=", ")
print("\n\n")

# Convert a dictionary(keys or values) into list

lst = list(name.values())
print("Values in list : ", lst)

lst1 = list(name.keys())
print("Keys in list : ", lst1)


