siswa = {"nama": "Oya", "kelas": "XI RPL", "nilai": 88}
print(siswa)
print(siswa["nama"])
print(siswa.get("hobi", "belum diisi"))
siswa["hobi"] = "membaca"
siswa["nilai"] = 90
del siswa["kelas"]
print(siswa)
