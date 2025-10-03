from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    
class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return self.base*self.height*0.5
    
class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side
    
    
r=rectangle(2,4)
t=triangle(3,4)
s=square(5)

print("Area of rectangle: ",r.area())
print("Area of triangle: ",t.area())
print("Area of square: ",s.area())