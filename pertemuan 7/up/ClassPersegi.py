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
