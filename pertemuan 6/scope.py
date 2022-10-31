# local scope
y = 10  # global variable


def fungsiSaya():
    global y  # memanggil global variable y
    global x  # membuat variable x menjadi global variabel
    x = 300
    # print(x + y)

    def fungsiDidalam():
        print(f"Cetak {x + y} dari fungsi Didalam dan Variabel dari luar fungsi")

    fungsiDidalam()


fungsiSaya()
print(f"cetak {y} global 1")
print(f"cetak {x} global 2")
