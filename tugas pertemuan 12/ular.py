from Animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super() .cetak()
        print("design \t\t: ", self.design,
              "\nracun \t\t: ", self.racun)
        
print('---- jenis ular----')

anaconda = ular("anaconda", "kambing", "semak-semak", "bertelur", "batik solo", "Tidak berbisa" )
anaconda.cetak_ular()

print('---- jenis ular----')

cobra = ular("cobra", "daging", "hutan", "bertelur", "corak kuning", "berbisa")
cobra.cetak_ular()