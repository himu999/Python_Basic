p = 50
k = "price is {}"
print(k.format(p))

b = "price is {:.2f} taka"
print(b.format(p))
quantity = int(input('qunatity : '))
itemno = int(input("itemno : "))
price = int(input("price : "))


order = "I want {} pieces of item number {} for {:.2f} dollars"

print(order.format(quantity, itemno, price), end="")

print()
age = 10
name = "himu"

bio = "His name is {1}. {1} is {0} years old"
print(bio.format(age, name))
