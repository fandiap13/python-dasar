class PersegiPanjang:
    nama = ''
    panjang = 0
    lebar = 0

    def __init__(self, nama, panjang, lebar):
        self.nama = nama
        self.panjang = panjang
        self.lebar = lebar

    def Luas(self):
        try:
            luas = float(self.panjang) * float(self.lebar)
            return luas
        except:
            return False

    def Keliling(self):
        try:
            keliling = 2 * (float(self.panjang) + float(self.lebar))
            return keliling
        except:
            return False
