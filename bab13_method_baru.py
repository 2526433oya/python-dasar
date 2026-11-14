class Orang:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        print("Halo, saya", self.nama)


class Siswa(Orang):
    def belajar(self):
        print(self.nama, "sedang belajar Python")


class Guru(Orang):
    def mengajar(self):
        print(self.nama, "sedang mengajar")


s = Siswa("Oya")
g = Guru("Pak Budi")
s.sapa()
s.belajar()
g.sapa()
g.mengajar()
