class Rapor:
    def __init__(self, pemilik, nilai):
        self.pemilik = pemilik
        self.__nilai = nilai

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai):
        if nilai in range(0, 101):
            self.__nilai = nilai
        else:
            print("Nilai harus 0 sampai 100")


r = Rapor("Oya", 85)
print(r.get_nilai())
r.set_nilai(95)
print(r.get_nilai())
r.set_nilai(150)
print(r.get_nilai())
