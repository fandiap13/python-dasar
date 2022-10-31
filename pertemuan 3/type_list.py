listData = ['budi', 5000, 'polpen']
# print(len(listNilai))   # mencari panjang data
# print(listNilai.count(6))   # mencari jumlah data yang muncul
# print(min(listNilai))   # mencari min data
# print(max(listNilai))   # mencari max data
# print(sum(listNilai))   # penjumlahan data list

# listNilai = [3, 4, 6, 5, 6, 4, 3, 2, 2]
# print(listNilai)
# print(listNilai[2])
# listNilai.sort(reverse=True)  # pengurutan data
# print(listNilai)
# print(listNilai[2])

# listNilai.reverse()   # membalik urutan

# print(listBuah[1])
# print(listNilai)

# listNilai.sort(reverse=True)
# print(listNilai)


# listBuah = ['apel', 'anggur', 'jeruk', 'jambu', 'semangka', 'melon']
# print(listBuah)
# listBuah[1] = 'kecubung'    # mengubah isi dari index ke 1
# print(listBuah)

# print(len(listBuah))
# print(listBuah[1:3])

# MENAMBAH DATA PADA INDEX
# listBuah.append('banana')   # menambah data pada bagian belakang list
# print(listBuah)
# listBuah.insert(1, 'Leci')    # menambah data pada index ke 1
# print(listBuah)

# MENGGABUNGKAN LIST
# listBuah = ['apel', 'anggur', 'jeruk', 'jambu', 'semangka', 'melon']
# listBuahPisang = ['pisang ambon', 'pisang kecubung', 'pisang ijo', 'pisang raja']

# # menggabungkan 2 list
# # kumpulanBuah = listBuah + listBuahPisang
# # print(kumpulanBuah)

# # untuk menambahkan list
# listBuah.extend(listBuahPisang)
# print(listBuah)

# # Untuk menghapus list sesuai dengan index
# del(listBuah[2])
# print(listBuah)

# # menghapus list sesuai nama value
# listBuah.remove('apel')
# print(listBuah)

# MENGHAPUS ITEM TERAKHIR
# listNilai = [3, 4, 6, 5, 6, 4, 3, 2, 2]
# print(listNilai)
# listNilai.pop()   # menghapus item terakhir
# print(listNilai)

# listNilai.sort()
# print(listNilai)

# listNilai.pop()
# print(listNilai)

# FUNGSI SPLIT, seperti expode
# kampusku = "Universitas Duta Bangsa"
# listKata = kampusku.split(' ')  # mengubah kata menjadi list
# print(listKata)
# print(len(listKata))

# kalimatPernyataan = "Saya belajar pyton, sambil makan, dengerin musik, sambil rebahan"
# pisahKalimat = kalimatPernyataan.split(',')
# print(pisahKalimat)
# print(len(pisahKalimat))

# FUNGSI JOIN, menggabungkan list menjadi kalimat / kata
listKata = ['saya', 'kuliah', 'di', 'UNS']
print(listKata)
tandaPemisah = '_#_'
tandaPemisah2 = '...'

hasilJoin = tandaPemisah.join(listKata)
hasilJoin2 = tandaPemisah2.join(listKata)

print(hasilJoin)
print(hasilJoin2)
