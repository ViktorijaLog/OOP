from datetime import*
class Dog:
    list_name=[]
    list_cena=[]
    def __init__(self, name=str,age=int,breed="unknow", weight=float, gender=str,cena= float, color="black"):
        self.name=name
        self.age=age
        self.breed=breed
        self.weight=weight
        self.gender=gender
        self.cena=cena
        self.color=color
        Dog. list_name.append(self.name)
        Dog.list_cena.append(self.cena)
    def print_info(self):
        print(f"Suņa vārds ir {self.name }, vecums {self.age},  šķirne {self.breed}, svars {self.weight}, dzimums {self.gender},cena {self.cena}, suņa krāsa {self.color}")
    def registration(self):
            now= datetime.now()
            dt_string=now.strftime("%d/%m/%Y/%H:%M:%S")
            print(f"Suns {self.name} ir reģistrēts {dt_string}")
    def piedalijas_konkursa(self,vieta):
         self.vieta=vieta
         print(f"Suns piedalījas konkursā {self.vieta}")
    def svars(self, svars1):
         self.svars1=svars1
         a=input("Vai suņa svars mainas? (palielinājās, samazinājās,nemainiījās)")
         if a== "samazinājās":
              self.weight-=self.svars1
              print(f"Svars  {self.weight}kg")
         if a== "palielinājās":
              self.weight+=self.svars1
              print(f"Svars  {self.weight}kg")
         if a== "nemainījās":
              print(f"Svars nemainījās {self.weight}kg")
    def vitaminu_skaits(self,daudzums):
         self.daudzums=daudzums
         skaits=self.weight/self.daudzums
         print(f"Vitamīnu doze ir {skaits}")

suns1=Dog ("Tobiks", 12, "Dog", 32, "v",250.00)
suns1.print_info()
suns2=Dog ("Tim", 5, "Dog", 10, "v",100.00)
suns2.print_info()
suns3=Dog ("Lion", 12, "Dog", 32, "v",250.00,"white")
suns3.print_info()
suns1.registration()
suns2.registration()
suns3.registration()
suns2.piedalijas_konkursa(1)
suns3.svars(2)
suns1.vitaminu_skaits(5)
print( f'suņa deva ir {round(skaits ,0)}') 