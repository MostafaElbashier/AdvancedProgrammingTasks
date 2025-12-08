class Vector3D: 
    def __init__(self, x, y, z): 
        self.x, self.y, self.z = x, y, z 
    def __add__(self, other): 
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z) 
    def __sub__(self, other): 
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z) 
    def __mul__(self, other): 
return self.x * other.x + self.y * other.y + self.z * other.z         
    def __repr__(self): 
        return f"Vector3D({self.x}, {self.y}, {self.z})" 
v1 = Vector3D(1, 2, 3) 
v2 = Vector3D(4, 5, 6) 
print(f"Add: {v1 + v2}")       
print(f"Sub: {v1 - v2}")        
print(f"Dot: {v1 * v2}")     
