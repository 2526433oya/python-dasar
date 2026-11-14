nilai = {"Matematika": 85, "Bahasa Indonesia": 90, "Pemrograman Web": 95}
for mapel in nilai:
    print(mapel)
for mapel, angka in nilai.items():
    print(mapel, "=", angka)
print(sum(nilai.values()) / len(nilai))
