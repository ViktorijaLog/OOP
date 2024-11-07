class Sacen:
    def __init__(self, name, surname, age, town):
        self.name=name
        self.surname=surname
        self.age=age
        self.town=town
    def print_info(self):
        print(f"Dalibnieka vārds ir {self.name }, uzvārds {self.surname}, vecums {self.age}, dalibnieks ir no {self.town} ")    
    def punkti(self):
        skaits1=int(input("Ievadiet punktu skaitu par 1.uzd:"))
        skaits2=int(input("Ievadiet punktu skaitu par 2.uzd:"))
        skaits3=int(input("Ievadiet punktu skaitu par 3.uzd:"))
        skaits4=int(input("Ievadiet punktu skaitu par 4.uzd:"))
        skaits5=int(input("Ievadiet punktu skaitu par 5.uzd:"))
        a=skaits1+skaits2+skaits3+skaits4+skaits5
        print(f"Kopā ir:{a}")

   ''' def diploms(self,skaits):
        self.skaits=skaits
        skaits=sum(self.punkti)
    if punkti>= 45:
        print(f'Saņemi 1.pakāpes diplomu!')
    elif: <40 punkti >=45:
        print('Saņemi 2.pakāpes diplomu!')
    else: <35 punkti >=30:
        print('Saņemi 3.pakāpes diplomu!')
    
    def premijas_summa(self,premija):
        self.premija=premija
        if 
        '''
        #VAR izdzēst to, kas ir aizkomentēts, tad viss strādas.
        #Varbūt doma bija pareiza,bet es aizmirsu,kas ir jādara 6 un 7.uzd.
   
    

            

   
dalibnieks1=Sacen("Ričards", "Zeils" ,12, "Rēzeknes")
dalibnieks1.print_info()
dalibnieks2=Sacen("Mihails", "Prančs", 15, "Daugavpils")
dalibnieks2.print_info()
dalibnieks3=Sacen("Lion", "Itkačs",18, "Jelgava") 
dalibnieks3.print_info()       
dalibnieks4=Sacen("Mārtiņš", "Taškāns",17, "Kuldīga") 
dalibnieks4.print_info()  
dalibnieks5=Sacen("Adrians", "Tučs",14, "Krāslava") 
dalibnieks5.print_info()  

dalibnieks1.punkti()
dalibnieks2.punkti()
dalibnieks3.punkti()    
dalibnieks4.punkti()
dalibnieks5.punkti()