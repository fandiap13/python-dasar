listMahasiswa = [60, 62, 63, 64, 70, 80, 61, 77, 55, 90, 100, 88, 99, 81, 44]

rata2 = int(sum(listMahasiswa)) / int(len(listMahasiswa))

print(
    f'Nilai terbesar = {max(listMahasiswa)}, Nilai terkecil = {min(listMahasiswa)}, Nilai rata - rata = {round(rata2, 2)}')
