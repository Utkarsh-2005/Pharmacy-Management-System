import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *

r=tk.Tk()
r.title('Medicine Database')
r.geometry('975x250')

connect = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'smartyutkarsh', database='cool', auth_plugin='mysql_native_password')

conn=connect.cursor(buffered=True)

conn.execute('SELECT*FROM medicine_database')

tree=ttk.Treeview(r)
tree['show']='headings'

s=ttk.Style(r)
s.theme_use('winnative')

#columns
tree['columns']=('refno','medname','medtype','slotno','quan','isdate','mandate','expdate','price')

#width
tree.column('refno', width=100, minwidth=100, anchor='center')
tree.column('medname', width=100, minwidth=100, anchor='c')
tree.column('medtype', width=100, minwidth=100, anchor='c')
tree.column('slotno', width=50, minwidth=50, anchor='c')
tree.column('quan', width=50, minwidth=50, anchor='c')
tree.column('isdate', width=150, minwidth=150, anchor='c')
tree.column('mandate', width=150, minwidth=150, anchor='c')
tree.column('expdate', width=150, minwidth=150, anchor='c')
tree.column('price', width=100, minwidth=100, anchor='c')

#heading names
tree.heading('refno',  text='ref. no', anchor='c')
tree.heading('medname',  text='Medicine Name', anchor='c')
tree.heading('medtype',  text='Medicine Type', anchor='c')
tree.heading('slotno',  text='Slot. No', anchor='c')
tree.heading('quan',  text='Quantity', anchor='c')
tree.heading('isdate',  text='Issued Date', anchor='c')
tree.heading('mandate',  text='Manufactured Date', anchor='c')
tree.heading('expdate',  text='Expiry Date', anchor='c')
tree.heading('price',  text='Price', anchor='c')

i=0
for ro in conn:
    tree.insert('', i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]))
    i=i+1
hsb = ttk.Scrollbar(r, orient='vertical')
hsb.configure(command=tree.yview)
tree.configure(yscrollcommand=hsb.set)
hsb.pack(fill='y',side ='right', expand='00')

tree.pack()

r.mainloop()
