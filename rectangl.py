'''class Rectangle:
    def __init__(self):
      self.width= int(input("Ievadiet platumu:"))
      self.height= int(input("Ievadiet garumu:"))

rect1=Rectangle()
rect1.width=100
rect1.height=200
print(f"{rect1.width}x{rect1.height}")
rect2=Rectangle()
print(f"{rect2.width}x{rect2.height}")'''

class Rectangle:
    def __init__(self,name, weight=10, height=20 ,color='blue'):
      self.width= width
      self.height=height
      self.color=color
      self.name=name

rect1=Rectangle("Square",100,100,orange)
print(f"{rect2.name}{rect2.color}{rect2.width}x{rect2.height}")
rect2=Rectangle('Rect')
print(f"{rect2.name}{rect2.color}{rect2.width}x{rect2.height}")

rectangles=[]
for i in range(100):
   rectangles.append(Rectangle('NAME'))

for rect in rectangles:
   print(f"{rect2.name}{rect2.color}{rect2.width}x{rect2.height}")