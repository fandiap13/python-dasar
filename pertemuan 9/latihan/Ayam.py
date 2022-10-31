from Hewan import Hewan
from Unggas import Unggas


class Ayam(Hewan, Unggas):
    def __init__(self, nama, sayap):
        self.nama = nama
        self.sayap = sayap

    def bisaBerkokok(self):
        print("bisa berkokok")
