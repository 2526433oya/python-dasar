count = 0
while count < 5:
    print("Hitung:", count)
    count += 1

for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
