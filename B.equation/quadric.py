# Quadric equation
# Negative sqrt can't be possible
# when your perform value proceed negative value into the sqrt function then compiler warn math domain error

import math
a, b, c = map(int, input("Enter the value of a, b , c = ").split())


D = math.sqrt(b*b-4*a*c)
x1 = (-b+D)/(2*a)
x2 = (-b-D)/(2*a)

print("x1 = ", x1)
print("x2 = ", x2)
