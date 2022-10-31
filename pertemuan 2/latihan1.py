klub = input("Masukkan Nama Klub : ")
jmlPertandingan = int(input("Jumlah Pertandingan : "))
jmlpertandinganMenang = int(input("Jumlah Pertandingan Menang : "))

presentaseMenang = (jmlpertandinganMenang / jmlPertandingan) * 100
presentaseKalah = 100 - presentaseMenang

print(
    f"Presentase pertandingan dari klub yg bernama {klub} adalah :\n - Kemenangan : {round(presentaseMenang, 2)} % \n - kekalahan {round(presentaseKalah, 2)} %")
