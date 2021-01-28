a = {"himel": "0185", "hasan": "7854", "halim": "014"}
x = a.get("himel")
print(x)
print(a.keys())

a["mama"] = "018"

print(a)

print(a.values())

a["hasan"] = "984"
print(a)

if 'himel' in a:
    print(True)