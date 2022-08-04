#import all the modules
from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("store.db")
c = conn.cursor()


result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]
    
class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="Add to the database", font=('arial 40 bold'),fg='steelblue')
        self.heading.place(x = 400,y=0)

        
         #labels and entries for window
        self.name_l =Label(master, text=" Enter Product Name", font =('arial 18 bold'))
        self.name_l.place(x=0, y=70)

        self.stock_l =Label(master, text=" Enter Stocks", font =('arial 18 bold'))
        self.stock_l.place(x=0, y=120)

        self.cp_l =Label(master, text=" Enter Cost Price", font =('arial 18 bold'))
        self.cp_l.place(x=0, y=170)

        self.sp_l =Label(master, text=" Enter Selling Price", font =('arial 18 bold'))
        self.sp_l.place(x=0, y=220)
        
        self.id_l=Label(master, text=" Enter ID", font =('arial 18 bold'))
        self.id_l.place(x=0, y=270)
        
        self.name_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.name_e.place(x=380 , y=70)

        self.stock_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.stock_e.place(x=380 , y=120)

        self.cp_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.cp_e.place(x=380 , y=170)

        self.sp_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.sp_e.place(x=380 , y=220)



        self.id_e = Entry(master, width = 25, font=('arial 18 bold'))
        self.id_e.place(x=380 , y=270)

        

        #button to add to the database
        self.btn_add = Button(master, text = "Add To Database", width =20, height=2,bg='steelblue',fg='white', command = self.get_items)
        self.btn_add.place(x = 560, y=420)
        
        #button to clear the entries
        self.btn_clear = Button(master, text = "Reset", width =20, height=2,bg='lightgreen',fg='white', command = self.clear_all)
        self.btn_clear.place(x = 380, y=420)
        
        #textbox for logs 
        self.tBox = Text(master, width=60,height=17)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END,"ID has reached upto: " + str(id))
        

        
        
        

    def clear_all(self,*args,**kwargs):
        
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.tBox.delete(END)
        self.id_e.delete(0,END)
    
    


    
    
    def get_items(self,*args, **kwargs):
        #get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        
        

        if self.name == '' or self.stock == '' or self.cp =='' or self.sp== '':
            print("empty")
            tkinter.messagebox.showinfo("Error","Please Fill all the entries.")
        else:
            #dynamic entries
            self.totalcp = float(self.cp) * float(self.stock)
            self.totalsp = float(self.sp) * float(self.stock)
            self.assumed_profit = float(self.totalsp - self.totalcp)
            sql = "INSERT INTO inventory(name, stock, cp, sp, totalcp, totalsp,  assumed_profit) VALUES(?,?,?,?,?,?,?)"
            c.execute(sql,(self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit))
            conn.commit()
            self.tBox.insert(END, "\n\nInserted " + str(self.name) + " into the database with code " + str(self.id_e.get()))
            print("good to go..")
            c.execute('SELECT * from inventory')
            print(c.fetchall())
            tkinter.messagebox.showinfo("Success","Successfully added to the database")
        
            








root =Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Add to the Database")
root.mainloop()
