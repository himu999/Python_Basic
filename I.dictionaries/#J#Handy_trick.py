a = {"name": "himu", "roll": "1", "class": "eight"}

for j, k in a.items():
    print("Keys : "+j+" | Values : "+k)

print("name" in a)
print("1" in a)
print("a" in a.keys())
print("a" in a.values())