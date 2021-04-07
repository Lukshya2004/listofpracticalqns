import mysql.connector
mydb = mysql.connector.connect(user = "root", host = "localhost", password = "thechick123", auth_plugin = "mysql_native_password")
mycursor = mydb.cursor()
mycursor.execute("use lukshya")
'''
mycursor.execute("desc movie")
for i in mycursor.fetchall():
    print(i)'''

'''record = ((234, 'yoyo', 2004, 'horror', 2), (234, 'yoyo', 2004, 'horror', 2), (234, 'yoyo', 2004, 'horror', 2), (234, 'yoyo', 2004, 'horror', 2))
mycursor.executemany("insert into movie values(%s, %s, %s, %s, %s)", record)
mydb.commit()'''

'''mycursor.execute("select * from movie where year < 2015")
for i in mycursor.fetchall():
    print(i)'''

'''movie_id = int(input('enter movie id here: '))
mycursor.execute(f"select * from movie where id = {movie_id}")
for i in mycursor.fetchall():
    print(i)'''

