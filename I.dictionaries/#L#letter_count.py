import pprint as pp
text = input()

d = {}

for k in text:

    d.setdefault(k, 0)
    d[k] = d[k] + 1

pp.pprint(d)
