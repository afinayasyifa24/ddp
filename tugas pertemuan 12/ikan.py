from Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, ciriKhas):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.ciriKhas = ciriKhas

    def cetak_ikan(self):
        super() .cetak()
        print("warna \t\t: ", self.warna,
              "\nciriKhas \t: ", self.ciriKhas)
        
print('---- jenis ikan----')

cupang = ikan("ikan cupang", "cacing sutra", "rawa-rawa", "bertelur", "biru", "memiliki warna corak yang indah" )
cupang.cetak_ikan()

print('---- jenis ikan----')

hiu = ikan("ikan hiu", "ikan-ikan kecil/anjing laut", "laut", "bertelur", "abu-abu", "memiliki gigi yang tajam dan taring" )
hiu.cetak_ikan()