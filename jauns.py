try:
    open('info.txt','r')
except:
    print("Tādas datnes nav, izveidosim")
    datne=open('info.txt','w')
def nolasaDrukaDatni():
    datne = open("info.txt")
    dati = datne.readline()
    rinda = dati.split(" ")
    print(rinda)
nolasaDrukaDatni()

menesi = ['janvaris', '31', 'februaris', '28', 'aprilis', '30']
with open('info.txt', 'w') as datne:
    for vards in menesi:
        datne.write(vards)
        datne.write(" ")
print('nolasu u n izdrukaju,atverot ar w')
nolasaDrukaDatni() 
open('info.txt','a')
print("\nnolasu un izdrukāju ierakstīto, atverot ar a")
nolasaDrukaDatni()
open('info.txt','w')
print("\nnolasu un izdrukāju ierakstīto, atverot ar w")
nolasaDrukaDatni()
datne.close()