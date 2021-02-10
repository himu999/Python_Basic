n = int(input("Check all the number from 0 to = "))

for i in range(0, n + 1):

    if i <= 1:
        print(f"{i} is not prime")

    else:
        for k in range(2, i, 1):
            if i % k == 0:
                print(f"{i} is not prime")
                break
        else:
            print(f"{i} is prime")
