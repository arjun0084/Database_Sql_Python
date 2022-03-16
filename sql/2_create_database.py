import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kshitij123"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase1")
for x in mycursor:
    print(x)