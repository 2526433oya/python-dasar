class Nilai:
    def __init__(self, mapel, angka):
        self.mapel = mapel
        self.angka = angka

    def tampil(self):
        print(self.mapel, "=", self.angka)

    def lulus(self):
        return self.angka >= 75

    def tambah(self, poin):
        self.angka += poin


n = Nilai("Pemrograman Web", 70)
n.tampil()
print(n.lulus())
n.tambah(10)
n.tampil()
print(n.lulus())
