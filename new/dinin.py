from logging import setLoggerClass
from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 


def main():
    win = Tk()
    app = dinin_details(win)
    win.mainloop()

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")

class dinin_details:

    def __init__(self,root):
        global cust_details_table
        self.root=root
        self.root.title("Customer details")
        self.root.geometry("1295x570+225+205")  

        global selected_items
        global se
        details_table=Frame(self.root,bd=5,bg="red",relief=RIDGE)
        details_table.place(x=10,y=50,width=1000,height=300) 

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("dinner_id","rm_no","meal_type","meal","quantity","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        selected_items = self.cust_details_table.selection()
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("dinner_id",text="order id")
        self.cust_details_table.heading("rm_no",text="RoomNo")
        self.cust_details_table.heading("meal_type",text="meal type")
        self.cust_details_table.heading("meal",text="meal")
        self.cust_details_table.heading("quantity",text="quantity")
        
        self.cust_details_table.heading("status",text="status")
        
        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("dinner_id",width=60)
        self.cust_details_table.column("rm_no",width=60)
        self.cust_details_table.column("meal_type",width=60)
        self.cust_details_table.column("meal",width=60)
        self.cust_details_table.column("quantity",width=60)
        
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
             my_cursor.execute("select*from dinner")
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
        my_cursor.execute(f"select * from dinner where status LIKE '%{se.get()}%'")
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
            query = "DELETE FROM dinner WHERE dinner_id =%s"
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
        #print(0,content[10])
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        con = content[0]
        my_cursor.execute("UPDATE dinner SET status='delievered' WHERE dinner_id="+content[0]
                                                    
                                                
                                                        

        )

        conn.commit()
        conn.close()

        messagebox.showinfo("sucess","Data updated successfully")
        content[0].delete(0,END)
'''
class login_window:
    def _init_(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0") ''' 

if __name__ == "__main__":
   main()