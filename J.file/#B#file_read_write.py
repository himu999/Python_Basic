f = open("read_write.txt", "a")
# f.write("s")
# f.write("k")
# f.write("who")

f.write("himu"+"\n")
# f.write()
f = open("read_write.txt", "r")
print(f.read())
f.close()

