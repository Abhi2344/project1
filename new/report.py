from logging import setLoggerClass
from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import os
from tkcalendar import DateEntry
conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class report:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Customer details")
        self.root.geometry("1295x570+225+205")  

        global selected_items
        global se
        global checidt
        global checodt
        details_table=Frame(self.root,bd=5,relief=RIDGE,bg="red")
        details_table.place(x=10,y=120,width=1000,height=300) 

        lab_Checkindetails =Label(self.root,text="from",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_Checkindetails.grid(row=11,column=0)

        # btnAdd=Button(lableframeleft,text="Date",font=("arial",12,"bold"),command=self.datefield,bg="black",fg="gold",width=9)
        # btnAdd.grid(row=2,column=1)
        checidt = StringVar()
        # enty_Checkindetails=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"),textvariable=checidt)
        # enty_Checkindetails.grid(row=2,column=1)
        enty_Checkindetails = DateEntry(self.root,width=40,date_pattern='dd/mm/Y',padx=2,pady=6,textvariable=checidt)
        enty_Checkindetails.grid(row=11,column=1)
 
        lab_checkoutdetails=Label(self.root,text="to",font=("consolas",12,"bold"),padx=2,pady=6)
        lab_checkoutdetails.grid(row=11,column=3)

        checodt = StringVar()
        # enty_checkoutdetails=ttk.Entry(lableframeleft,width=29,font=("arial",13,"bold"),textvariable=checodt)
        # enty_checkoutdetails.grid(row=3,column=1)
        enty_checkoutdetails = DateEntry(self.root,width=40,date_pattern='dd/mm/Y',padx=2,pady=6,textvariable=checodt)
        enty_checkoutdetails.grid(row=11,column=5)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("book_id","cust_contact","cust_ema","chein_date","cheout_date","rm_type","av_room","n_day","n_eld","n_chld","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        selected_items = self.cust_details_table.selection()
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("book_id",text="Booking id")
        self.cust_details_table.heading("cust_contact",text="customer contact")
        self.cust_details_table.heading("cust_ema",text="customer email")
        self.cust_details_table.heading("chein_date",text="checkin date")
        self.cust_details_table.heading("cheout_date",text="checkout date")
        self.cust_details_table.heading("rm_type",text="room type")
        self.cust_details_table.heading("av_room",text="avialable room")
        self.cust_details_table.heading("n_day",text="no of day")
        self.cust_details_table.heading("n_eld",text="no of elders")
        self.cust_details_table.heading("n_chld",text="no of child")
       
        self.cust_details_table.heading("status",text="status")
        
        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("book_id",width=60)
        self.cust_details_table.column("cust_contact",width=60)
        self.cust_details_table.column("cust_ema",width=60)
        self.cust_details_table.column("chein_date",width=60)
        self.cust_details_table.column("cheout_date",width=60)
        self.cust_details_table.column("rm_type",width=60)
        self.cust_details_table.column("av_room",width=60)
        self.cust_details_table.column("n_day",width=60)
        self.cust_details_table.column("n_eld",width=60)
        self.cust_details_table.column("n_chld",width=60)
        
        self.cust_details_table.column("status",width=60)
        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        # self.cust_details_table.bind("<ButtonRelease-1>",self.cursor)
        self.fetch_data()

        regbutton=Button(self.root,text="search by checkin date",font=("consolas",9,"bold"),command=self.showbd,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=620,y=0,width=170,height=35)
        regbutton=Button(self.root,text="search by checkout date",font=("consolas",9,"bold"),command=self.showbout,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=800,y=0,width=170,height=35)

        # se=StringVar()
        # self.flno=ttk.Entry(self.root,font=("consolas",10,"bold"),textvariable=se)
        # self.flno.place(x=140,y=380,width=200)
        # regbutton=Button(self.root,text="Delete",font=("consolas",15,"bold"),command=self.mDelete,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        # regbutton.place(x=480,y=370,width=120,height=35)

        # regbutton=Button(self.root,text="update",font=("consolas",15,"bold"),command=self.cursor,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        # regbutton.place(x=620,y=370,width=120,height=35)
        self.showbd()
        # self.cursor()
    def fetch_data(self):
             conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
             my_cursor=conn.cursor()
             my_cursor.execute("select*from cust_booking")
             rows=my_cursor.fetchall()
             if len(rows)!=0:
                 self.cust_details_table.delete(*self.cust_details_table.get_children())
                 for i in rows:
                     self.cust_details_table.insert("",END,values=i)
                 conn.commit
             conn.close()
    

    def showbd(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select * from cust_booking where chein_date between %s and %s",[checidt.get(),checodt.get()])
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
        conn.commit
        conn.close()

    def showbout(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select * from cust_booking where cheout_date between %s and %s",[checidt.get(),checodt.get()])
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
        conn.commit
        conn.close()


        

if __name__ == "__main__":
    root = Tk()
    obj= report(root)
    root.mainloop()