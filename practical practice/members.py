import mysql.connector
mydb = mysql.connector.connect(user = "root", host = "localhost", password = "thechick123", auth_plugin = "mysql_native_password")
mycursor = mydb.cursor()
mycursor.execute("use lukshya")
record = ('lukshya', 20000)
mycursor.execute("insert into emp values(%s, %s)", record)
mydb.commit()