"""
Rules of scope:
1) we can't use the local variables inside the global scope
2) But local scopes can use the global variables
3) We can use same name for both the local and global variables, but not a good practice and often leads to ambiguity
def f():
    c = 10
    print(c)
print(c)
##can't use the local variables inside the global scope
"""


def fun(a):

    print(a)


fun(45)
