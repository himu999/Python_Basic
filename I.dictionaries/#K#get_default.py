a = {"name": "himu", "roll": "1", "class": "eight"}

print(str(a.get("roll", "Default")), end=" ")
print(str(a.get("rol", "Default")), end=" ")
print(str(a.get("rolll", 5)))

print(a.setdefault("name", "df"), end=" ")
print(a.setdefault("color", "yellow"))

print(a)
