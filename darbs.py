class kafijas_automata_klase:
 def __init__(self,marka,uznemums):
              self.marka=marka
              self.uznemums=uznemums
 def pagatavot_kafiju(self,kafijas_veids):
       print(f'Pagatavo kafiju {self.kafijas_veids} no kafijas automāta {self.marka}')
 def uznemuma_info(self):
       print(f'Kafija tika pagatavota no markas {self.marka} ko ražo uzņēmums {self.uznemums}')
kafijas_automāts=("LAVAZZ")
kafijas_automāts.pagatavot_kafiju('Ecspreso')
kafijas_automāta.uzņēmuma_info()
