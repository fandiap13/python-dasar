class PersegiPanjang:
    nama = ''
    panjang = 0
    lebar = 0

    def __init__(self, nama, panjang, lebar):
        self.nama = nama
        self.panjang = panjang
        self.lebar = lebar

    def Luas(self):
        luas = self.panjang * self.lebar
        return luas

    def Keliling(self):
        keliling = 2 * (self.panjang + self.lebar)
        return keliling


class Persegi:
    nama = ""
    panjangSisi = 0

    def __init__(self, nama, panjangSisi):
        self.nama = nama
        self.panjangSisi = panjangSisi

    def Luas(self):
        luas = self.panjangSisi * self.panjangSisi
        return luas

    def Keliling(self):
        keliling = 4 * self.panjangSisi
        return keliling


print("========= Selamat datang di program sederhana =========")
print("==================== Bangun Ruang =====================")

print("Mau menghitung apa ? ")
print("1. Persegi")
print("2. Persegi Panjang")

pilihan = int(input("Masukkan pilihan : "))

if pilihan == 1:
    print("Anda memilih persegi")
    nama = input("Masukkan nama bangun : ")
    panjangSisi = int(input("Masukkan panjang sisi : "))

    PersegiObj = Persegi(nama, panjangSisi)
    print(f"{PersegiObj.nama} memiliki sisi: {PersegiObj.panjangSisi}, luas: {PersegiObj.Luas()}, keliling: {PersegiObj.Keliling()}")

elif pilihan == 2:
    print("Anda memilih persegi panjang")
    nama = input("Masukkan nama bangun : ")
    panjang = int(input("Masukkan panjang : "))
    lebar = int(input("Masukkan lebar : "))

    PersegiPanjangObj = PersegiPanjang(nama, panjang, lebar)
    print(f"{PersegiPanjangObj.nama} memiliki panjang: {PersegiPanjangObj.panjang}, lebar: {PersegiPanjangObj.lebar}, luas: {PersegiPanjangObj.Luas()}, keliling: {PersegiPanjangObj.Keliling()}")

else:
    print(f"Pilihan {pilihan} tidak tersedia")
