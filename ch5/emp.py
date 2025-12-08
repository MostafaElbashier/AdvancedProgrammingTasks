class Employee: 
    def __init__(self , id , name , salary): 
        self.employee_id = id 
        self.name = name 
        self.salary = salary 
 
    @classmethod 
    def from_string(cls , employee_str): 
        vals = employee_str.split(',')  
   return cls(vals[1] , vals[0] , vals[2]) 
     
    def display_employee_info(self): 
        print(f"Id: {self.employee_id} , Name: {self.name} , Salary: {self.salary}") 
 
 
emp = Employee.from_string("John Doe,E123,50000") 
 
emp.display_employee_info() # Id: E123 , Name: John Doe , Salary: 50000 
