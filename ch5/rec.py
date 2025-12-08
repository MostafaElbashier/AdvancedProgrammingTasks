class Rectangle: 
    def __init__(self , w , h): 
        self.width = w 
        self.height = h 
    def area(self): 
        return self.width * self.height 
    def perimeter(self): 
        return (self.width + self.height) * 2   
rec = Rectangle(5 , 2) 
print(rec.area())  
print(rec.perimeter()) # 14
