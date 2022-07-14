import mysql.connector
import os

mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'smartyutkarsh', database='cool', auth_plugin='mysql_native_password')
cursor=mydb.cursor(buffered=True)
cursor.execute('create table if not exists meds(s int(2),q int(2), l int(3))')
cursor.execute('desc Medicine_Database')
for x in cursor:
    print(x)
file = open('x.txt',"r")
file_data = file.read()
file_data = file_data.split('\n')
a  = int(file_data[0])
b  = file_data[1]
i  = file_data[2]
c  = int(file_data[3])
d  = int(file_data[4])
e  = file_data[5]
f  = file_data[6]
g  = file_data[7]
h  = int(file_data[8])
file.close()
cursor.execute("INSERT INTO Medicine_Database VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (a , b, i, c, d, e, f, g, h))
mydb.commit()
cursor.execute('select*from Medicine_Database')
for x in cursor:
    print(x)
os.remove('x.txt')
os.system('table.py')
