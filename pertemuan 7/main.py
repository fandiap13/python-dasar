from ClassPersegiPanjang import PersegiPanjang
from ClassPersegi import Persegi

print("========= Selamat datang di program sederhana =========")
print("==================== Bangun Ruang =====================")

print("\n")

print("Mau menghitung apa ? ")
print("1. Persegi")
print("2. Persegi Panjang")

pilihan = input("Masukkan pilihan : ")

if pilihan == "1":
    print("Anda memilih persegi")
    nama = input("Masukkan nama bangun : ")
    panjangSisi = input("Masukkan panjang sisi : ")

    PersegiObj = Persegi(nama, panjangSisi)
    if PersegiObj.Luas() and PersegiObj.Keliling():
        print(f"{PersegiObj.nama} memiliki sisi: {PersegiObj.panjangSisi}, luas: {PersegiObj.Luas()}, keliling: {PersegiObj.Keliling()}")
    else:
        print("Input panjang sisi tidak valid")

elif pilihan == "2":
    print("Anda memilih persegi panjang")
    nama = input("Masukkan nama bangun : ")
    panjang = input("Masukkan panjang : ")
    lebar = input("Masukkan lebar : ")

    PersegiPanjangObj = PersegiPanjang(nama, panjang, lebar)
    if PersegiPanjangObj.Luas() and PersegiPanjangObj.Keliling():
        print(f"{PersegiPanjangObj.nama} memiliki panjang: {PersegiPanjangObj.panjang}, lebar: {PersegiPanjangObj.lebar}, luas: {PersegiPanjangObj.Luas()}, keliling: {PersegiPanjangObj.Keliling()}")
    else:
        print("Input panjang dan lebar tidak valid")

else:
    print(f"Pilihan {pilihan} tidak tersedia")
