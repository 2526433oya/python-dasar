def cek_nilai(nilai):
    if nilai < 0:
        raise ValueError("Nilai tidak boleh negatif!")
    else:
        print("Nilai valid:", nilai)


try:
    cek_nilai(-5)
except ValueError as e:
    print("Error:", e)
