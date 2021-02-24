a = {1: 1, 2: 2, 3: 1, 4: 34}

b = {}
count = {}

for i in a.values():
    count.setdefault(i, 0)
    # print("before = ", count[i])
    count[i] = count[i] + 1
    # print(count[i])
#
# print(count)

i = 0
for k, v in count.items():
    if v == 1:
        b.update({i: k})
        i = i + 1
for i in b.values():
    print(i, end=" ")