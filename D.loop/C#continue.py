# Simple Code using continue statement
while True:
    name = input("Who are you? : ")

    if name != "Rafi":
        continue
    print("Hello there "+name+". What is the passcode? ")
    passcode = input("Enter your pass code : ")
    if passcode == "12345":
        break

print("Mama now let's play cricket")
