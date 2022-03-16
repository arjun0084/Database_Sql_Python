import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kshitij123",
    database="mydatabase1"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")
mycursor.execute("SHOW FIELDS")


#IF runns without any error table sucessfully created