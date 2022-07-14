#Imports
from tkinter import*
from tkinter import ttk
import os
import sys
from PIL import ImageTk, Image

def main():

    #Main screen
    Master = Tk()
    Master.title('Pharmacy management system')
    Master.geometry('1355x620')
    #Vars
    e1=StringVar()
    e2=StringVar()
    e3=StringVar()
    e4=StringVar()
    e5=StringVar()
    e6=StringVar()
    e7=StringVar()
    e8=StringVar()
    e9=StringVar()

    #Functions
    def add():
        refno=e1.get()
        medname=e2.get()
        medtype=e9.get()
        slotno=e3.get()
        quan=e4.get()
        isdate=e5.get()
        mandate=e6.get()
        expdate=e7.get()
        price=e8.get()
        vam = open('x.txt',"w")
        vam.write(refno+'\n')
        vam.write(medname+'\n')
        vam.write(medtype+'\n')
        vam.write(slotno+'\n')
        vam.write(quan+'\n')
        vam.write(isdate+'\n')
        vam.write(mandate+'\n')
        vam.write(expdate+'\n')
        vam.write(price+'\n')
        vam.write('0')
        vam.close()
        os.system('add.py')

    def update():
        refno=e1.get()
        medname=e2.get()
        medtype=e9.get()
        slotno=e3.get()
        quan=e4.get()
        isdate=e5.get()
        mandate=e6.get()
        expdate=e7.get()
        price=e8.get()
        vam = open('x.txt',"w")
        vam.write(refno+'\n')
        vam.write(medname+'\n')
        vam.write(medtype+'\n')
        vam.write(slotno+'\n')
        vam.write(quan+'\n')
        vam.write(isdate+'\n')
        vam.write(mandate+'\n')
        vam.write(expdate+'\n')
        vam.write(price+'\n')
        vam.write('0')
        vam.close()
        os.system('update.py')

    def delete():
        refno=e1.get()
        vam = open('x.txt',"w")
        vam.write(refno)
        vam.close()
        os.system('delete.py')
        
    def reset():
        print('cleared')
        Master.destroy()
        main()

    def display():
        os.system('table.py')


    #Main Screen Labels
    Label(Master, text="Pharmacy management system",bd=10,fg='dark green',bg='white',relief=SOLID, font=('Arial',50,'bold')).grid(row=3,sticky=W,pady=5,padx=175)

    #Frames
    DataFrame=Frame(Master,bd=10,relief=SOLID,padx=20)
    DataFrame.place(x=2,y=120,width=1350,height=400)

    DataFrameLabel=LabelFrame(DataFrame,bd=7,relief=SOLID,padx=20,text="Dashboard",fg="red",font=("arial",12,'bold'))
    DataFrameLabel.place(x=0,y=5,width=800,height=365)

    #Buttons Frame
    ButtonFrame=LabelFrame(Master,bd=7,relief=SOLID,padx=20,text="Functions",fg="red",font=("arial",12,'bold'))
    ButtonFrame.place(x=2,y=520,width=1350,height=60)

    #Buttons
    Button(ButtonFrame, text='        Add        ',fg ='black',font=('Arial',10,'bold'), command=add).grid(row=0,column=0)
    Button(ButtonFrame, text='        Update        ',fg ='black',font=('Arial',10,'bold'), command=update).grid(row=0,column=1)
    Button(ButtonFrame, text='        Delete        ',fg ='black',font=('Arial',10,'bold'), command=delete).grid(row=0,column=2)
    Button(ButtonFrame, text='        Reset        ',fg ='black',font=('Arial',10,'bold'), command=reset).grid(row=0,column=3)
    Button(ButtonFrame, text='        Exit        ',fg ='black',font=('Arial',10,'bold'), command=Master.destroy).grid(row=0,column=4)
    Button(ButtonFrame, text='        Dislpay        ',fg ='black',font=('Arial',10,'bold'), command=display).grid(row=0,column=5)

    #Search Label Combo box Entry


    #Dashboard Labels

    referenceno=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Reference No.').grid(row=2,column=0,sticky=W)

    MedicineName=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Medicine Name').grid(row=3,column=0,sticky=W)

    Type=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Medicine Type').grid(row=4,column=0,sticky=W)

    Slot=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Slot No.').grid(row=5,column=0,sticky=W)

    Quantity=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Quantity').grid(row=6,column=0,sticky=W)

    Issuedate=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Issued Date (YYYY/MM/DD)').grid(row=7,column=0,sticky=W)

    Manufacturedate=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Manufactured Date (YYYY/MM/DD)').grid(row=8,column=0,sticky=W)

    Expirydate=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Expiry Date (YYYY/MM/DD)').grid(row=9,column=0,sticky=W)

    Price=Label(DataFrameLabel, font=('Arial',21,'italic'), fg='black', text='Price').grid(row=10,column=0,sticky=W)

    #Dashboard Comboboxes

    ref_combo=Entry(DataFrameLabel, width=25, font=('Arial',15), relief=SOLID, bd=2, textvariable=e1)
    ref_combo.grid(row=2,column=1)

    type_combo=ttk.Combobox(DataFrameLabel, width=25, font=('Arial',15), state="readonly", textvariable=e9)
    type_combo["values"]=("Liquid","Tablet","Capsule","Topical medicines","Suppositories","Drops","Inhalers","Injections","Patches")
    type_combo.grid(row=4,column=1)
    type_combo.current(0)

    name_combo=Entry(DataFrameLabel, width=25, font=('Arial',15), relief=SOLID, bd=2, textvariable=e2)
    name_combo.grid(row=3,column=1)

    #Dashboard Entries

    Entry(DataFrameLabel, fg='black', font=('Arial',17), width=10, relief=SOLID, bd=2, textvariable=e3).grid(row=5, column=1, sticky=W)

    Entry(DataFrameLabel, fg='black', font=('Arial',17), width=10, relief=SOLID, bd=2, textvariable=e4).grid(row=6, column=1, sticky=W)

    Entry(DataFrameLabel, fg='black', font=('Arial',17), width=10, relief=SOLID, bd=2, textvariable=e5).grid(row=7, column=1, sticky=W)

    Entry(DataFrameLabel, fg='black', font=('Arial',17), width=10, relief=SOLID, bd=2, textvariable=e6).grid(row=8, column=1, sticky=W)

    Entry(DataFrameLabel, fg='black', font=('Arial',17), width=10, relief=SOLID, bd=2, textvariable=e7).grid(row=9, column=1, sticky=W)

    Entry(DataFrameLabel, fg='black', font=('Arial',17), width=10, relief=SOLID, bd=2, textvariable=e8).grid(row=10, column=1, sticky=W)

  
    #End
    medicine_table=ttk.Treeview

    #Image import
    img = Image.open('pharmacy.png')
    img = img.resize((460,370))
    img = ImageTk.PhotoImage(img)
    Label(DataFrame, image=img).grid(padx=820,pady=0)



    Master.mainloop()
main()
