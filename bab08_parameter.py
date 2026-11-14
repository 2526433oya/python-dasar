def perkenalan(nama, kelas="XI RPL"):
    print("Nama:", nama, "Kelas:", kelas)


def min_max(angka):
    return min(angka), max(angka)


perkenalan("Oya")
perkenalan("Budi", "XI TKJ")
perkenalan(kelas="X RPL", nama="Sari")
terendah, tertinggi = min_max([80, 95, 70])
print(terendah, tertinggi)
