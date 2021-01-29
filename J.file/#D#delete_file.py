import os

f = open("file.txt", "w")
f.close()
# os.remove("file.txt")

if os.path.exists("file.txt"):
    os.remove("file.txt")
    print("Successfully file deleted")
else:
    print("The file does not exist")

# To delete an entire folder, use the os.rmdir()
# os.rmdir
