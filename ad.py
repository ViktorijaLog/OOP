'''datne= open ("admin.txt")
print(datne.read(5))
datne.seek(0)
print(datne.read(5))
pos=datne.tell()
print("Kursos atrodas uz",pos," simbola")
datne.seek(0)
print(datne.read(5))
print("Kursos atrodas uz",datne.tell()," simbola")'''

'''datne= open ("admin.txt")
viss=datne.readlines()
print('viss=', vssi)''' 

datne = open('a.txt')
sum=0
s=[]
"""
print('uyytyty')
print(
datne.read
(5))
datne.seek
(0)
print(
datne.read
(5))
pos = datne.tell()
print('Kursors atrodas uz', datne.tell(),'simbols')
viss = datne.readlines()
print('viss=', viss)
print('viss=', end='')
"""
for rinda in datne:
    print('rinda=', rinda)
    sarakstaDati = rinda.split(" ")
    vards=sarakstaDati[0]
    print('vards=', vards)
    vecums=sarakstaDati[3]
    print('vecums=', vecums)
    dati = rinda.split(" ")
    sum += int(sarakstaDati[3])
    s.append(sarakstaDati[3])
    vid = sum/len(s)
print("sum = ", sum)
print('VID VECUMS',vid)
datne.close() 