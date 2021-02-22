def hcf(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a

    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            ann = i
1
    print("HCF : ", ann)


k = int(input("First number : "))
j = int(input("Second number : "))

hcf(k, j)
