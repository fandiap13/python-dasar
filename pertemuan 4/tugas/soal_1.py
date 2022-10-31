nama = input("Masukkan nama anda : ")
tahun = int(input('Masukkan tahun kelahiran anda : '))

if tahun >= 1944 and tahun <= 1964:
    kategori = "Baby boomer"
elif tahun >= 1965 and tahun <= 1979:
    kategori = "Generasi X"
elif tahun >= 1980 and tahun <= 1994:
    kategori = "Generasi Y (Millenials)"
elif tahun >= 1995 and tahun <= 2015:
    kategori = "Generasi Z"
else:
    kategori = "belum terkategori kan"

print(f'{nama} berdasarkan tahun lahir anda tergolong generasi {kategori}')
