class Orang:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        print("Halo, saya", self.nama)


class Siswa(Orang):
    pass


s = Siswa("Oya")
s.sapa()
print(isinstance(s, Orang))
print(issubclass(Siswa, Orang))
