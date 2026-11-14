class Orang:
    def __init__(self, nama):
        self.nama = nama


class Siswa(Orang):
    def __init__(self, nama, kelas):
        super().__init__(nama)
        self.kelas = kelas

    def tampil(self):
        print(self.nama, "dari kelas", self.kelas)


s = Siswa("Oya", "XI RPL")
s.tampil()
