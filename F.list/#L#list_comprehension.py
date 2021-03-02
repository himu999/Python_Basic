fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [expression for item in iterable if condition == True]

lst = [x for x in fruits if "a" in x]

print(lst)

lst1 = [x for x in fruits if "a" not in x]
print(lst1)

lst2 = [m.upper() for m in fruits]
print(lst2)

lst3 = [z.capitalize() for z in fruits]
print(lst3)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst4 = [k for k in a if k % 2 == 0]
print(lst4)
