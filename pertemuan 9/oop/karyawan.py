class Karyawan:
    nomorId = 0
    nama = 'nama standar karyawan'
    status = 'kontrak'

    def presensiMasuk(self):
        print(f"{self.nama} melakukan presensi masuk")

    def presensiKeluar(self):
        print(f"{self.nama} melakukan presensi keluar")
