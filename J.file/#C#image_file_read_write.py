f = open("img.jpg", "rb")

# print(f.read())
"""
    for data in f.read():
    print(data)
"""

f1 = open("img1.jpg", "wb")

for data in f:
    f1.write(data)
f1.close()
f.close()
