class Vehicle: 
    def move(self): 
        print("vehicle is moving...") 
class Car(Vehicle): 
    def move(self): 
        print("car is driving...") 
class Bike(Vehicle): 
    def move(self): 
        print("bike is cycling...") 
vehicles = [Vehicle() , Car() , Bike()] 
for v in vehicles: 
    v.move()
