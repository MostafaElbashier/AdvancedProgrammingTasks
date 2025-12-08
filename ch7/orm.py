from sqlalchemy import create_engine, Column, Integer, String, Float 
from sqlalchemy.orm import declarative_base, sessionmaker 
Base = declarative_base() 
class Student(Base): 
__tablename__ = "students" 
id = Column(Integer, primary_key=True) 
name = Column(String(100)) 
grade = Column(Float) 
def __repr__(self): 
return f"Student(id={self.id}, name='{self.name}', grade={self.grade})" 
engine = 
create_engine("mysql+mysqlconnector://root:your_password@localhost/school") 
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine) 
session = Session() 
student1 = Student(name="Mohamed", grade=88.5) 
student2 = Student(name="Guido", grade=91.2) 
session.add_all([student1, student2]) 
session.commit() 
students = session.query(Student).all() 
for s in students: 
print(s)
