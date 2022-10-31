class Pekerjaan:
    gaji = 0
    namaPekerjaan = ""

    def __init__(self, namaPekerjaan, gaji):
        self.gaji = gaji
        self.namaPekerjaan = namaPekerjaan
        print(f"{self.namaPekerjaan} gajinya {self.gaji}")
