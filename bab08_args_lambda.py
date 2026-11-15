def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)


jumlahkan(1, 2, 3, 4, 5)


def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


biodata(nama="Oya", kelas="XI RPL", kota="Subang")
