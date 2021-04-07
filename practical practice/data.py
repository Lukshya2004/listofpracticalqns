import mysql.connector
mydb = mysql.connector.connect(user = "root", host = "localhost", password = "thechick123", auth_plugin = "mysql_native_password")
mycursor = mydb.cursor()
mycursor.execute("use lukshya")
mycursor.execute("select * from emp where empid < 10")
for i in mycursor.fetcall():
    print(i)