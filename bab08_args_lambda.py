def jumlah(*angka):
    return sum(angka)


def profil(**data):
    for k, v in data.items():
        print(k, "=", v)


kuadrat = lambda x: x * x
print(jumlah(1, 2, 3, 4))
profil(nama="Oya", kelas="XI RPL")
print(kuadrat(7))
print(list(map(lambda n: n + 1, [1, 2, 3])))
