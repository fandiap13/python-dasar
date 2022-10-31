perulangan = 100
counter = 1

while counter <= perulangan:
    if counter == 50:
        hasil = 'Minum dulu'
    elif counter == 100:
        hasil = f'Capek'
    else:
        hasil = f'push up ke {counter}'
    print(hasil)
    counter += 1
