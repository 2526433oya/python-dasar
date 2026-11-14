hadir = 85
if hadir >= 90:
    print("Kehadiran sangat baik")
elif hadir >= 75:
    print("Kehadiran baik")
else:
    print("Kehadiran kurang")
status = "Lulus" if hadir >= 75 else "Tidak lulus"
print(status)
