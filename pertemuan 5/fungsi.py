# fungsi

# print('Halo selamat pagi, hari ini kita akan belajar tentang fungsi di pyton')
# print('Halo selamat siang, hari ini kita akan belajar tentang fungsi di pyton')
# print('Halo selamat sore, hari ini kita akan belajar tentang fungsi di pyton')
# print('Halo selamat malam, hari ini kita akan belajar tentang fungsi di pyton')


# def ucapSelamant(waktu, nama):
#     print(
#         f'Halo selamat {waktu} {nama}, hari ini kita akan belajar tentang fungsi di pyton')


# nama = input("Masukkan nama anda : ")
# waktu = input('Masukkan waktu sekarang pagi/siang/sore/malam : ')

# ucapSelamant(waktu, nama)


# def hitungLuasPersegiPanjang(panjang, lebar):
#     luas = float(panjang)*float(lebar)
#     print(f"Luas dari {panjang} dan lebar {lebar} adalah {luas}")


# panjang = int(input('Masukkan panjang : '))
# lebar = int(input('Masukkan lebar : '))

# hitungLuasPersegiPanjang(panjang, lebar)


# def hitungLuasPersegiPanjang(panjang, lebar):
#     luas = float(panjang)*float(lebar)
#     return luas


# panjang = int(input('Masukkan panjang : '))
# lebar = int(input('Masukkan lebar : '))

# hasil = hitungLuasPersegiPanjang(panjang, lebar)
# print(f'Luas dari panjang {panjang} dan lebar {lebar} adalah {hasil}')


# def hitungBangun(namaBangun, panjang, lebar):
#     luas = panjang * lebar
#     return f"Luas {namaBangun} dengan panjang {panjang} dan lebar {lebar} adalah {luas}"


# namaBangun = input('Masukkan nama bangun : ')
# panjang = float(input('Masukkan panjang : '))
# lebar = float(input('Masukkan lebar : '))

# hasil = hitungBangun(namaBangun, panjang, lebar)
# print(hasil)

# FUNGSI DIDALAM FUNGSI
# def hitungBangunPersegiPanjang():
#     panjang = input('masukkan panjang : ')
#     lebar = input('masukkan lebar : ')

#     def hitungLuas(panjang, lebar):
#         return float(panjang)*float(lebar)

#     def hitungKeliling(panjang, lebar):
#         return 2*(float(panjang) + float(lebar))

#     luas = hitungLuas(panjang, lebar)
#     keliling = hitungKeliling(panjang, lebar)

#     print(f'Luas dari panjang {panjang} dan lebar {lebar} adalah {luas}')
#     print(
#         f'Keliling dari panjang {panjang} dan lebar {lebar} adalah {keliling}')


# hitungBangunPersegiPanjang()


def tambah(angka1, angka2):
    hasil = angka1+angka2
    return hasil


def kurang(angka1, angka2):
    hasil = angka1-angka2
    return hasil


def kali(angka1, angka2):
    hasil = angka1*angka2
    return hasil


def bagi(angka1, angka2):
    hasil = angka1/angka2
    return hasil


def output():
    print("============================= OUTPUT =============================")


print("====== KALKULATOR SEDERHANA ======")
angka1 = float(input("Masukkan angka - 1 = "))
angka2 = float(input("Masukkan angka - 2 = "))
pilihFungsi = input("Masukkan operator(+, *, -, /) : ")

if pilihFungsi == "+":
    hasil = tambah(angka1, angka2)
elif pilihFungsi == "-":
    hasil = kurang(angka1, angka2)
elif pilihFungsi == "*":
    hasil = kali(angka1, angka2)
elif pilihFungsi == "/":
    hasil = bagi(angka1, angka2)
else:
    output()
    print("Operator yang anda masukkan tidak valid")
    exit()


output()
print(f"Hasil dari {angka1} {pilihFungsi} {angka2} adalah {hasil}")
