# Remember year must be greater than 1581

year = int(input("Select a random year : "))

if year <= 1581:
    print("Year must be greater than : 1581")
elif (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, " : is a leap year")
else:
    print(year, " : is not a leap year")
