import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password ='Anuj@190603',
    database = 'python_db'
)

mycursor = mydb.cursor()

mycursor.execute('show databases')
for x in mycursor:
    print(x)

mycursor.execute('''create table cupboard(
 id int(15) not null,
 name varchar(75) not null,
 price float not null,
 count int not null,
 primary key(id)
)''')

mycursor.execute("show tables")
for x in mycursor:
 print(x)

mycursor.execute('''insert into cupboard(id, name, price, count)
values (6, 'cb31', 7500, 8)''')
mydb.commit()
print(mycursor.rowcount,'records inserted')
