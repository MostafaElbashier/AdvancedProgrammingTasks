class Shape: 
    def area(self): 
        return 0 
class Rectangle(Shape): 
    def __init__(self , w , h): 
        self.width = w 
self.height = h 
def area(self): 
return self.width * self.height 
class Circle(Shape): 
def __init__(self , r): 
self.radius = r 
def area(self): 
return math.pi * (self.radius ** 2) 
# the main function: 
def print_shape_area(shape): 
print(f"the area of this shape is {shape.area()}") 
shape = Shape() 
rec = Rectangle(3 , 4) 
circle = Circle(4) 
print_shape_area(shape) 
print_shape_area(rec) 
print_shape_area(circle)
