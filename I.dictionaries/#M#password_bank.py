pb = {"Himu": 12345, "Rimu": 45678, "Simu": 78912}
i = 0
while i < 5:
    name = input("Enter your name : ")

    if name in pb:

        for k in range(0, 3):
            password = int(input("Enter your password : "))
            if password in pb.values():
                print("Login successful")
                break
            else:
                print("Password doesn't matched try again")
    else:
        print("there is no such name!! try again ")

    i = i + 1
