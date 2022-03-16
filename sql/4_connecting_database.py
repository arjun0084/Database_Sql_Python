#trying to connect to database
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kshitij123",
    database="mydatabase1"
)
#if it runs without any error the "mydatabase1" exist on pc and you are sucessfully connected to database