'''class kafijas_automata_klase:
 def __init__(self,marka,uznemums):
              self.marka=marka
              self.uznemums=uznemums
 def pagatavot_kafiju(self,kafijas_veids):
       print(f'Pagatavo kafiju {self.kafijas_veids} no kafijas automāta {self.marka}')
 def uznemuma_info(self):
       print(f'Kafija tika pagatavota no markas {self.marka} ko ražo uzņēmums {self.uznemums}')
kafijas_automāts=("LAVAZZ")
kafijas_automāts.pagatavot_kafiju('Ecspreso')
print uznemuma_info()'''

class Telefons:
      def __init__(self,zime,modelis,cena):
            self.zime=zime
            self.modelis=modelis
            self.cena=cena

      def atlaide1(self,atlaide):
            self.atlaide=atlaide

            if (self.cena)> 400:
                  cena1=self.cena-(self.cena*self.atlaide/100)
                  print(f'Atlaide {cena1}')
            else: 
                  print('Atlaides nav')


      def paradit_info(self):
            print(f'Telefons {self.zime} modelis{self.modelis}')
      def iestatit_tonu(self, jauns_tonis):
            self.jauns_tonis=jauns_tonis
            print(f'Telefona jaunais tonis ir {self.jauns_tonis}')
telef1=Telefons('Samsung','A24', 340)
telef1.paradit_info()
telef1.iestatit_tonu('Bing-bong')
telef1.atlaide1(20)