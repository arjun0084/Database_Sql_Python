import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kshitij123",
    database="mydatabase1"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)