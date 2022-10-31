from pekerjaan_detail import Pekerjaan
from karyawan_file import Karyawan

Karyawan1 = Karyawan()
Karyawan1.nomorId = 1
Karyawan1.nama = "Fandi"
Karyawan1.status = "Karyawan tetap"

Karyawan2 = Karyawan()
Karyawan2.nomorId = 2
Karyawan2.nama = "Aziz"
Karyawan2.status = "Karyawan abadi"


print("Karyawan 1 : ", Karyawan1.nama)
print("Karyawan 2 : ", Karyawan2.nama)
Karyawan1.presensiMasuk()
Karyawan2.presensiMasuk()

Pekerjaan1 = Pekerjaan('Pro gamer', 100000000000)
print("Pekerjaan : ", Pekerjaan1.nama)
print("Gaji : ", Pekerjaan1.gaji)
