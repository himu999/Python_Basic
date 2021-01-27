family = {"parents", "sibling", "sweet memory", "home"}
relatives = {"cousin", "nephew", "niece", "uncle", "Aunt"}

family.update(relatives)

print("Member of family : ", family)

a = {"a", "b", "c", "d", "e", 1}
b = {1, 2, 3, 4, 5, "a"}
c = a.union(b)
print("Element of c set : ", c)

d = {"e", "f", "g", "h", "i", 5}
e = {5, 6, 7, 8, 9, "e"}

'''
d.intersection_update(e)
print(d)
'''

z = e.intersection(d)
print(z)

f = {"apple", "google", "amazon", "github", "play store", "huawei", "rayzon", "facebook"}
g = {"microsoft", "intel", "rayzon", "facebook", "huawei",  "play store", "github"}

g.symmetric_difference_update(f)
print("element of g : ", g)

h = {"apple", "google", "amazon", "github", "play store", "huawei", "rayzon", "facebook"}
i = {"microsoft", "intel", "rayzon", "facebook", "huawei",  "play store", "github"}

k = h.symmetric_difference(i)

print("Element of k : ", k)
