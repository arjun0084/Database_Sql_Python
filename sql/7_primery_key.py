'''
Primary Key

When creating a table, you should also create a column with a unique key for each record.

This can be done by defaning a PRIMARY KEY.

We use the statement HINT AUTO INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.
'''

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kshitij123",
    database="mydatabase1"
)

mycursor=mydb.cursor()

#for new database
# mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")

# for existing database
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")