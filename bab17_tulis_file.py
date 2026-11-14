file = open("data.txt", "w")
file.write("Halo, ini data Oya!\n")
file.write("Baris kedua...\n")
file.close()

file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()
print("Selesai menulis data.txt")
