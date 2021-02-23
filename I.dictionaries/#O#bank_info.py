bank_usr = {"Himu": 132, "Rafi": 933, "Jimi": 456}

print("Welcome to the bank")
print("What do you like to do?")
print(" " + '1.view balance')
print(" " + '2.view all bank info')
print(" " + '3.update balance')
print(" " + '4.exit')

while True:

    number = input("Select your operation : ")

    if number == '1':
        name = input("Enter costumer name : ")
        if name in bank_usr.keys():
            print(name + " balance is ", bank_usr[name])
        else:
            print("The user can't found! would you like to add the user to the account?")
            cond = input("Give your opinion : ")
            if cond == "Yes":
                name1 = input("Enter costumer name : ")
                balance = input("Enter costumer balance : ")
                bank_usr.update({name1: balance})

            else:
                print("Would you like to exit?")
                cond1 = input("Give your opinion : ")
                if cond1 == "Yes":
                    break
    elif number == "2":
        for k, v in bank_usr.items():
            print("User name : ", k + " | " + "Balance =", v)

    elif number == "3":
        name = input("Enter your name : ")
        if name in bank_usr.keys():
            print("Do you want to add or subtract form costumer savings?")
            cond2 = input("Give your opinion : ")

            if cond2 == "Add":
                current_balance = bank_usr[name]
                amount = int(input("Enter amount you want to add : "))
                new_balance = current_balance + amount
                bank_usr.update({name: new_balance})
                print("Balance updated! costumer current balance is :", bank_usr[name])

            elif cond2 == "Subtract":
                current_balance = bank_usr[name]
                amount = int(input("Enter amount you want to add : "))
                new_balance = current_balance - amount
                bank_usr.update({name: new_balance})
                print("Balance updated! costumer current balance is :", bank_usr[name])
        else:
            print("There is no such account in the bank database!!")
    elif number == "4":
        break





