class Vector: 
    def __init__(self , x , y): 
        self.x = x 
        self.y = y 
    def __sub__(self , other): 
        return Vector(self.x - other.x , self.y - other.y) 
    def __mul__(self , other): 
        return Vector(self.x * other.x , self.y * other.y) 
    def printVec(self): 
        print(f"({self.x} , {self.y})") 
v1 = Vector(1 , 2) 
v2 = Vector(3 , 4) 
ex1 = v2 - v1 
ex2 = v2 * v1 
ex1.printVec() -> (2 ,2) 
ex2.printVec() -> (3 ,8)
