a = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
c = [9, 5, 7, 25, 74, 98, 35]
d = ["orange", "Mango", "Kiwi", "pineapple", "Banana"]

b.sort(reverse=True)
c.sort()
a.sort()
print("Element of a: ", a)
# Case sensitive
a.sort(key=str.lower)
print("Element of c : ", c)
print("Element of b : ", b)
