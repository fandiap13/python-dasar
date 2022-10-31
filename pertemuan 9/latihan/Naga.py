from Hewan import Hewan
from Unggas import Unggas
from Mamalia import Mamalia
from Fantasy import Fantasy


class Naga(Hewan, Unggas, Mamalia, Fantasy):
    def __init__(self, nama, sayap, kaki):
        self.nama = nama
        self.sayap = sayap
        self.kaki = kaki

    def bisaTerbang(self):
        print("Bisa terbang")
