from logging import setLoggerClass
from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import os

def main():
    win = Tk()
    app = bok_details(win)
    win.mainloop()

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")

class bok_details:

    def __init__(self,root):
        global cust_details_table
        self.root=root
        self.root.title("Customer details")
        self.root.geometry("1295x570+225+205")  

        global selected_items
        global se
        details_table=Frame(self.root,bd=5,relief=RIDGE,bg="red")
        details_table.place(x=10,y=50,width=1000,height=300) 

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
        self.cust_details_table.bind("<ButtonRelease-1>",self.cursor)
        self.fetch_data()

        regbutton=Button(self.root,text="search",font=("consolas",15,"bold"),command=self.showbd,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=10,y=370,width=120,height=35)

        se=StringVar()
        self.flno=ttk.Entry(self.root,font=("consolas",10,"bold"),textvariable=se)
        self.flno.place(x=140,y=380,width=200)
        regbutton=Button(self.root,text="Delete",font=("consolas",15,"bold"),command=self.mDelete,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=480,y=370,width=120,height=35)

        regbutton=Button(self.root,text="update",font=("consolas",15,"bold"),command=self.cursor,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=620,y=370,width=120,height=35)
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
        my_cursor.execute(f"select * from cust_booking where status LIKE '%{se.get()}%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
        conn.commit
        conn.close()


    def mDelete(self):
       
        selected_item = self.cust_details_table.selection()[0]
        # print(self.cust_details_table.item(selected_item)['values'])
        bid = self.cust_details_table.item(selected_item)['values'][0]
        
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            query = "DELETE FROM cust_booking WHERE book_id =%s"
            value = (bid,)
            rs = my_cursor.execute(query,value)
           
            
            conn.commit()
            self.cust_details_table.delete(selected_item)
            conn.close()
            messagebox.showinfo("success","Data deleted successfully",parent=self.root)

            
        except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
    #     # mDelete = messagebox.askyesno("Delete","Do you want to delete this record")
    #     # if mDelete>0:
    #     #     conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
    #     #     my_cursor=conn.cursor()
    #     #     query = "delete from cust_reg email=%s"
    #     #     value = (self.em)
    def cursor(self):
        cursor_row=self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row,"values")
        print(content)
        #print(0,content[9])
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        con = content[0]
        print(content[4])
        if content[10]=='booking pending':

            my_cursor.execute("UPDATE cust_booking SET status='booking confirm' WHERE book_id="+content[0]
       
                                                    
                                                
                                                        

            )
            conn.commit()
            conn.close()
        
            op=messagebox.showinfo("sucess","Data updated successfully",parent=self.root)
            content[0].delete(0,END)
        elif content[10]=='booking confirm':
            my_cursor.execute("UPDATE cust_booking SET status='avialable' WHERE book_id="+content[0]


            )
            conn.commit()
            conn.close()
        
            op=messagebox.showinfo("sucess","Data updated successfully",parent=self.root)
            content[0].delete(0,END)


            

        else:
            messagebox.showinfo("error","")
        if op==True:

            self.root.destroy()
            os.system("python customerhome.py")
'''
class login_window:
    def _init_(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0") ''' 

if __name__ == "__main__":
   main()