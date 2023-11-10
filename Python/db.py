import mysql.connector

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anuj@190603"
)

# Create a database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# Use the database
mycursor.execute("USE mydatabase")

# Create a table
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Insert single row
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()

# Insert multiple rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345')
]
mycursor.executemany(sql, val)
mydb.commit()

# Display rows
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Update values
sql = "UPDATE customers SET address = 'Canyon 123' WHERE name = 'John'"
mycursor.execute(sql)
mydb.commit()

# Search for a record
sql = "SELECT * FROM customers WHERE name = 'John'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
if myresult:
    print("Record found")
else:
    print("Record not found")

# Alter table
mycursor.execute("ALTER TABLE customers ADD COLUMN email VARCHAR(255)")

# Delete rows
sql = "DELETE FROM customers WHERE name = 'John'"
mycursor.execute(sql)
mydb.commit()

# Delete table
# mycursor.execute("DROP TABLE customers")

# Delete database
#mycursor.execute("DROP DATABASE mydatabase")

# Close the connection
mydb.close()



