import pymysql 
 
connect = pymysql.connectect( 
    host="localhost", 
    user="root", 
    password="your_password", 
    database="school" 
) 
curson = connect.cursonsor() 
try: 
    connect.start_transaction() 
    curson.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",("Omar", 90)) 
    curson.execute("INSERT INTO students (name, grade) VALUES (%s, %s)",("Laila", 95)) 
    connect.commit() 
 
except Exception as e: 
    print("Error:", e) 
    connect.rollback() 
    print("Transaction rolled back!") 
curson.execute("SELECT * FROM students") 
for row in curson.fetchall(): 
    print(row) 
curson.close() 
connect.close()
