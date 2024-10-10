'''class MyClass:
    name="Tests"

    #Konstruktors
    def_init_(self):
    pass
#Metode
def getName():
    return name 

programma'''

class Color:
    red = 0
    green = 0
    blue = 0

    def    __init__(self, r,g,b):
        self.red=r
        self.green=g
        self.blue=b
        print(r,g,b)

    def info_print(self,r,g,b):
        print(f'Red {r} green{g} blue {b}')
    def toHex(self):
        return '#%02x%02x%02x' % (
self.red
, 
self.green
, 
self.blue
)
    def redColor(self):
        self.red=255
        for i in range(20):
            print(self.red-i, self.green, self.blue)


gray = Color(0,128,0)  
gray.info_print(0,128,0)      
print(gray.toHex()) 
print(gray.redColor())