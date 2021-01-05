def prime(num):
    if num == 0 or num == 1:
        print("Number is : ", num)
    elif num > 1:
        for i in range(2, num//2):
            if num % i == 0:
                print(num, " : is not a prime number")
                break
            else:
                print(num, " : is a prime number")
                break
    else:
        print(num, " : is a negative number")


prime(int(input("Enter your number : ")))
