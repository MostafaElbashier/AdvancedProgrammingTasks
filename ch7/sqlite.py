connect = pymysql.connect( 
host="localhost", 
user="root", 
password="your_password", 
database="school" 
) 
cur = connect.cursor() 
cur.execute(""" 
CREATE TABLE IF NOT EXISTS students ( 
id INT AUTO_INCREMENT PRIMARY KEY, 
name VARCHAR(100), 
grade FLOAT 
) 
""") 
students = [("Ali", 85.5),("Sara", 92.0),("Mohamed", 78.3)] 
cur.executemany("INSERT INTO students (name, grade) VALUES (%s, %s)", students) 
connect.commit() 
cur.execute("SELECT * FROM students") 
rows = cur.fetchall() 
for row in rows: 
print(row) 
connect.close()
