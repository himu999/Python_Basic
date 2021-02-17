import random

# float number generator between 0 and 1
b = random.random()
print(b)

# random number generator

c = random.randint(0, 50)
print(c)

# random number with rand range function

d = random.randrange(100)

print(d)

# 10 random number between 100 and 3000

e = random.sample(range(10, 3000), 10)

print(e)
