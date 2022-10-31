from karyawan import Karyawan
from pekerjaan import Pekerjaan

class AdminKeuangan(Karyawan, Pekerjaan):
    def mendataGaji(self):
        print('sedang mendata gaji.....')
