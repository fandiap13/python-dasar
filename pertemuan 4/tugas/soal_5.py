nama = input("Masukkan nama anda : ")
nilaiInputan = 7
daftarNilai = []

for i in range(nilaiInputan):
    nilai = int(input(f'Masukkan nilai ke - {i + 1} : '))
    daftarNilai.append(nilai)

rata2 = sum(daftarNilai) / len(daftarNilai)

print("\n=============Output=============")
print(f"Nama mahasiswa : {nama}")
print(f"Daftar nilai = {daftarNilai}")
print(f"Nilai tertinggi = {max(daftarNilai)}")
print(f"Nilai terendah = {min(daftarNilai)}")
print(f"Nilai rata-rata = {round(rata2, 3)}")
