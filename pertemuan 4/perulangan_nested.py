# perulangan for didalam for

# for number1 in range(1, 10):
#     for number2 in range(number1, 10):
#         print(number1, number2)

# listCoffe = ['latte', 'kopi tubruk', 'abc coffe', 'torabika', 'top coffe']
# listType = ['es', 'panas']

# for tipe in listType:
#     for kopi in listCoffe:
#         menu = f"{tipe} {kopi}"
#         if menu == "es kopi tubruk" or menu == 'panas kopi tubruk':
#             print(f'{menu} habis')
#         else:
#             print(menu)

# while else
# jmlJamMain = 0
# while jmlJamMain < 5:
#     jmlJamMain += 1
#     print(f"andi main baru {jmlJamMain} jam")
# else:
#     print(f'andi hanya boleh main {jmlJamMain} jam')

# for else
listNama = ['budi', 'andi']
listPenyakit = ['kadas', 'kurap', 'panu', 'kutu ari']

for nama in listNama:
    for penyakit in listPenyakit:
        print(f'{nama} suka kena {penyakit}')
else:
    print(f'ternyata {listNama[0]} dan {listNama[1]} suka sakit')
