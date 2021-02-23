dictionary = {"Himu": 12345, "Rupa": 45600, "Rafi": 12000, "Mania": 2000}
i = 1
while i <= 5:
    name = input("Enter the name (To exit press enter): ")

    if name == "":
        break
    else:
        if name in dictionary:
            print(name, " : ", dictionary[name])
        else:
            print("There is no such name in the phonebook!!")
    i = i + 1
