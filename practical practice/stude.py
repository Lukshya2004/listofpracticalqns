import mysql.connector
mydb = mysql.connector.connect(user = "root", host = "localhost", password = "thechick123", auth_plugin = "mysql_native_password")
mycursor = mydb.cursor()
mycursor.execute("use lukshya")
try:
    mycursor.execute("create table stud(rollno int, name varchar(50), age int, city varchar(100))")
    mycursor.execute("create table marks(rollno int, eng int, math int, phy int, chem int, cs int)")
except:
    print("tables already exist")

record = (16, 'luksh', 17, 'oman')
mycursor.execute("insert into stud values(%s,%s,%s,%s)", record)

mydb.commit()
