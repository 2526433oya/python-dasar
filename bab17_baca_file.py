file = open("data.txt", "r")
print(file.read())
file.close()

file = open("data.txt", "r")
for baris in file:
    print(baris.strip())
file.close()
