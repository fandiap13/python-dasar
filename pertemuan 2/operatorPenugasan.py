# # operator +=
# angkaPertama = 7
# angkaPertama += 2
# # a += b
# # a + b = ...

# operator -=
angkaPertama = 7
angkaPertama -= 2
# a -= b
# a - b = ...

# operator %=
# %= digunakan untuk menghitung sisa bagi
angkaPertama = 5
angkaPertama %= 2
# a %= b
# a % b = ...

# print(angkaPertama)


# Menghitung panjang karakter (jml karakter)
# kampusKu = 'Universitas Sebelas Maret'
# print(len(kampusKu))
# print(kampusKu[2])  # dimulai dari 0: 0,1,2,3 dst...
# output : i
# print(kampusKu[-2])  # dimulai dari 1:1,30,29 dst...
# output : e

# kampusKu = "Duta Bangsa Surakarta"
# print(f"{kampusKu[4:12]}{ kampusKu[-2:-1]}")

# print(kampusKu[3:8])
# output : versi

# pencarian
# print(kampusKu.find('Maret'))
# output : 20, berarti kata Maret terdapat pada index ke 20

# Operasi string
kampusKu = "universitas duta bangsa"
lokasi = " surakarta "

print(kampusKu.upper())
print(kampusKu.lower())
print(kampusKu.title())
print(kampusKu.capitalize())

print(len(lokasi))
print(lokasi.rstrip())
print(len(lokasi.rstrip()))
print(lokasi.lstrip())
print(len(lokasi.lstrip()))

print(len(lokasi.lstrip().rstrip()))  # output 9
print(lokasi.lstrip().rstrip().capitalize())  # output: surakarta
