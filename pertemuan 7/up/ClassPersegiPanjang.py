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
