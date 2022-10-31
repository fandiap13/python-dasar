def tambah(angka1, angka2):
    try:
        hasil = int(angka1) + int(angka2)
        return hasil
    except:
        print("Anda harus memasukkan angka !")
    # finally:
    #     print('Cek error finish')


nomor1 = input("Masukkan nomor ke 1 :")
nomor2 = input("Masukkan nomor ke 1 :")

hasil = tambah(nomor1, nomor2)
print(f"hasil={hasil}")
