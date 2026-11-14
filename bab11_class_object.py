class Siswa:
    sekolah = "SMKN 2 Subang"

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas


s1 = Siswa("Oya", "XI RPL")
s2 = Siswa("Budi", "XI TKJ")
print(s1.nama, s1.kelas)
print(s2.nama, s2.kelas)
print(s1.sekolah)
print(type(s1))
