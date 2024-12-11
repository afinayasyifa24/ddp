from Animal import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, suara):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.suara = suara

    def cetak_burung(self):
        super() .cetak()
        print("jenis \t\t: ", self.jenis,
              "\nsuara \t\t: ", self.suara)
        
print('---- jenis burung----')

gereja = burung("burung gereja", "biji jagung", "amazon", "bertelur", " Southern grey-headed sparrow", "cit cit" )
gereja.cetak_burung()

print('---- jenis burung----')

elang = burung("burung elang", "serangga dan ulat", "di wilayah berlereng", "bertelur", "elang jawa", "huohuoo")
elang.cetak_burung()