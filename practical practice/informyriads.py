import mysql.connector
mydb = mysql.connector.connect(user = "root", host = "localhost", password = "thechick123", auth_plugin = "mysql_native_password")
mycursor = mydb.cursor()
mycursor.execute("use lukshya")
'''
mycursor.execute("select * from emp where salary > 6000")
for i in mycursor.fetchall():
    print(i)'''

'''mycursor.execute("update emp set salary = salary + 1000 where salary < 8000")
mydb.commit()'''

'''money = int(input("enter salary to be deleted here: "))
mycursor.execute(f"delete from emp where salary = {money} ")
mydb.commit()'''

'''mycursor.execute("select * from emp order by salary")
for i in mycursor.fetchall():
    print(i)'''

name = input("enter name of employee to be deleted here: ")
mycursor.execute(f"delete from emp where name = '{name}' ")
mydb.commit()