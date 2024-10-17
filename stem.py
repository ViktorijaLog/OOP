from random import*

class STEM:
    def rectangle_area(width=1, height=1):
        if width>0 and height>0:
         print(f"The area is {abs(width)*(height)}")
        else:
           print(f"Can not calculate negative area {width*height}")
for i in range(20):
    w=randint(-20,20)
    h=randint(-20,20)
    STEM.rectangle_area(w,h)