# stripping

a = '   Bangladesh is my motherland    '
print(a)
print(a.lstrip())

b = ' Bangladesh is my motherland      '
print(b)
print(b.rstrip())
print(b.lstrip())


a = '   Bangladesh is my motherland  '
print(a)
print(a.strip())

# replace
print("\n")
a = 'Himel is a simple boy'
old = 'simple'
new = 'good'
str =  a.replace(old, new)
print(str)

b = 'Amader akash'
old = "Amader akash"
new= "tmdr batash"

c = b.replace(old, new)
print(b)
print(c)
