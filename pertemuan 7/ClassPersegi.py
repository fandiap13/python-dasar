class Persegi:
    nama = ""
    panjangSisi = 0

    def __init__(self, nama, panjangSisi):
        self.nama = nama
        self.panjangSisi = panjangSisi

    def Luas(self):
        try:
            luas = float(self.panjangSisi) * float(self.panjangSisi)
            return luas
        except:
            return False

    def Keliling(self):
        try:
            keliling = 4 * float(self.panjangSisi)
            return keliling
        except:
            return False
