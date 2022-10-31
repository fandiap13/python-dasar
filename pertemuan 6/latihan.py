def cekLogin(username, password):
    if username == 'budi' and password == '1235':
        return "Berhasil login"
    else:
        return 'Gagal login'


username = input('Masukkan username : ')
password = input('Masukkan password : ')

cekLogin = cekLogin(username, password)

# if(cekLogin == True) :
#   print("Berhasil login")
# else:
#   print("Gagal login")

print(cekLogin)