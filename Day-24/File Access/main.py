file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

#a - append
#w - creates file if not present
with open("my_file.txt",mode="a") as f:
    f.write("\nsimply")