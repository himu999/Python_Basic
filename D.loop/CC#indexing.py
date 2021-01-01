"""
For loop structure:
for variable in (range function):
    -----
    -----
range(3) - loop will run three times, starting is zero unless specified
range(0,3) - loop will run 3-1 times that is 0,1,2
range(0,10,2) - loop will run from 0 to 10-1 times and step size of the loop variable will increase by 2

"""

for i in range(1):
    print("Happy New year")
print("###Integer value###")
for i in range(1, 31):
    print(i, end=" ")
print(end="\n")
print("###Odd number###")
for i in range(1, 30+1, 1):
    if i % 2 != 0:
        print(i, end=" ")
print()
# for new line
print("###Even number###")
for i in range(1, 30+1, 1):
    if i % 2 == 0:
        print(i, end=" ")
