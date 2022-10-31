pengulangan = 5
i = 1

print("Mengecek bilangan genap atau ganjil")

while i <= pengulangan:
    nilai = int(input(f"Masukkan bilangan ke - {i} : "))
    if nilai % 2 == 0:
        print(f"Angka {nilai} adalah bilangan Ganjil")
    else:
        print(f"Angka {nilai} adalah bilangan Genap")
    i += 1
else:
    print("=============Selesai=============")
