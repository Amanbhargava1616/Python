with open("read.txt") as r:
    content = r.read()
print(content)

with open("write.txt") as w:
    print(f"Old content of write file: {w.read()}")

with open("write.txt", "w") as w:
    w.write("Old content in this file will be replaced by new content")
    print("Writting complete")

with open("new_file.txt", "x") as x:
    x.write("This is a new file, which is created")
