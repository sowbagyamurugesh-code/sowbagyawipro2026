import mysql.connector
host="localhost"
user="root"
password="root"
database="wipro2026"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("connected to the database successfully")

#query="SELECT * FROM employee"
query="INSERT INTO `wipro2026`.`employee`(`Empid`,`Empname`,`Salary`) VALUES (103,'sri',45000);"
cursor.execute(query)
conn.commit()
print("1 row inserted successfully")


result=cursor.fetchall()

for row in result:
    print(row)