import mysql.connector
import os

mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'smartyutkarsh', database='cool', auth_plugin='mysql_native_password')
cursor=mydb.cursor(buffered=True)
for x in cursor:
    print(x)
file = open('x.txt',"r")
file_data = file.read()
a  = int(file_data)
file.close()
sql_Delete_query = """delete from Medicine_Database where refno = %s"""
cursor.execute(sql_Delete_query, (a,))
mydb.commit()
cursor.execute('select*from Medicine_Database')
for x in cursor:
    print(x)

os.remove('x.txt')
os.system('table.py')
