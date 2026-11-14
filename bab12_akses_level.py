class Akun:
    def __init__(self):
        self.nama = "Oya"
        self._status = "aktif"
        self.__kode = "abc"


a = Akun()
print(a.nama)
print(a._status)
try:
    print(a.__kode)
except AttributeError:
    print("Atribut private tidak bisa diakses langsung")
