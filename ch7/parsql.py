connect = pymysql.connect( 
host="localhost", 
user="root", 
password="your_password", 
database="school" 
) 
curson = connect.cursor() 
name = input("Enter name: ") 
grade = float(input("Enter grade: ")) 
curson.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",(name, grade)) 
connect.commit() 
curson.execute("SELECT * FROM students") 
for row in curson.fetchall(): 
print(row) 
curson.close() 
connect.close()
