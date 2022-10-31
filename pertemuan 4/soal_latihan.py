nama = input("Masukkan Nama : ")
tahun = int(input('Masukkan tahun kelahiran : '))


if tahun >= 1944 and tahun <= 1964:
    kategori = "Baby boomer"
elif tahun >= 1965 and tahun <= 1979:
    kategori = "Generasi X"
elif tahun >= 1980 and tahun <= 1994:
    kategori = "Generasi Y"
elif tahun > 1995 and tahun <= 2015:
    kategori = "Generasi Z"
else:
    kategori = "Belum terkategorikan"

print(f'{nama} berdasarkan tahun lahir anda tergolong generasi {kategori}')


# nama = input('Masukkan nama : ')
# beratBadan = int(input('Masukkan berat badan (kg) : '))
# tinggiBadan = int(input('Masukkan tinggi badan (cm) : '))

# bmi = beratBadan / ((tinggiBadan / 100) ** 2)

# if bmi < 18.5:
#     kategori = 'Kurus'
# elif bmi >= 18.5 and bmi < 25:
#     kategori = 'Langsing/sehat'
# else:
#     kategori = 'Gemuk'

# print(f'Nilai BMI anda adalah : {round(bmi, 3)}')
# print(f'{nama} anda tergolong berbadan {kategori}')
