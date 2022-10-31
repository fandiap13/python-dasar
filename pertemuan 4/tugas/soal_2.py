beratBadan = int(input('Masukkan berat badan anda (kg) : '))
tinggiBadan = int(input('Masukkan tinggi badan anda (cm) : '))

bmi = beratBadan / ((tinggiBadan / 100) ** 2)

if bmi < 18.5:
    kategori = 'Terlalu kurus'
elif bmi >= 18.5 and bmi < 25:
    kategori = 'Langsing/sehat'
else:
    kategori = 'Gemuk'

print(f'Nilai BMI anda adalah : {round(bmi, 3)}')
print(f'Anda tergolong berbadan {kategori}')
