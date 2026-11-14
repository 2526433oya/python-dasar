hari = ("Senin", "Selasa", "Rabu")
print(hari)
print(hari[0])
print(len(hari))
a, b, c = hari
print(a, b, c)
try:
    hari[0] = "Minggu"
except TypeError:
    print("Tuple tidak bisa diubah")
