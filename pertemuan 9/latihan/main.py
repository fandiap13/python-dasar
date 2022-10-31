from Ayam import Ayam
from Naga import Naga


AyamObj = Ayam("Ayam betina", 2)
print("Nama : ", AyamObj.nama)
print("Sayap : ", AyamObj.sayap)
AyamObj.bisaBertelur()
AyamObj.bisaBerkokok()

print('='*30)

NagaObj = Naga("Dragon", 2, 4)
print("Nama : ", NagaObj.nama)
print("Sayap : ", NagaObj.sayap)
print("Kaki : ", NagaObj.kaki)
NagaObj.bisaMenyemburkanApi()
NagaObj.bisaTerbang()
