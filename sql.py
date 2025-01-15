import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()

table_info = """create table STUDENT(Name varchar(10), Class varchar(10), Section varchar(10), Marks int)""" 

cursor.execute(table_info)

cursor.execute("insert into STUDENT values('Rahul', 'X', 'A', 90)")
cursor.execute("insert into STUDENT values('Rohit', 'X', 'B', 85)")
cursor.execute("insert into STUDENT values('Raj', 'X', 'C', 80)")
cursor.execute("insert into STUDENT values('Ravi', 'X', 'D', 75)")
cursor.execute("insert into STUDENT values('Rahul', 'X', 'A', 90)")

print("The inserted records are")

data = cursor.execute("select * from STUDENT")

for i in data:
    print(i)

connection.commit()
connection.close()