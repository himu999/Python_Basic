def fun(a):

    if a == 1:

        return a
    else:
        return a + fun(a-1)


n = int(input("Enter the number of series : "))

print(fun(n))
