datne= open ("admin.txt")
print(datne.read(5))
datne.seek(0)
print(datne.read(5))
pos=datne.tell()
print("Kursos atrodas uz",pos," simbola")
datne.seek(0)
print(datne.read(5))
print("Kursos atrodas uz",datne.tell()," simbola")'