'''class Nolasa:
  with open('admin.txt','r') as datne:
    dati=datne.readline()
    sarakstaDati=dati.split(" ")
    vards=sarakstaDati[0]
    print("sarakstaDati=", sarakstaDati)
    print("vards=" ,vards)
    for vards in sarakstaDati:
     print(vards)'''

class Nolasa:
    def __init__(self, nosaukums):
        self.nosaukums=nosaukums
    def nolasaDatus(self, nasaukums):
        print("nosaukums=", self.nosaukums)
    with open("admin.txt") as datne:
        dati=datne.readline()
        sD=dati.split(" ")
        vards=sD[0]
        print("sd=", sD)
        print("vards=", vards)
        for vards in sD:
            print(vards) 