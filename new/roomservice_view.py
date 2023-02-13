from logging import setLoggerClass
import re
from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import base64

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class rms_view:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer details")
        self.root.geometry("1295x570+225+205")  
        global selected_item
        global se
        details_table=Frame(self.root,bd=5,relief=RIDGE,bg="red")
        details_table.place(x=10,y=50,width=1000,height=300) 

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("ser_id","rm_no","des","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        selected_item = self.cust_details_table.selection()
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ser_id",text="service id")
        self.cust_details_table.heading("rm_no",text="Room no")
        self.cust_details_table.heading("des",text="Descripton")
        self.cust_details_table.heading("status",text="status")

        
        
        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("ser_id",width=60)
        self.cust_details_table.column("rm_no",width=60)
       
        self.cust_details_table.column("des",width=60)
        self.cust_details_table.column("status",width=60)
        
        
        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        regbutton=Button(self.root,text="search",font=("consolas",15,"bold"),command=self.showrs,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=10,y=370,width=120,height=35)

        se=StringVar()
        self.flno=ttk.Entry(self.root,font=("consolas",10,"bold"),textvariable=se)
        self.flno.place(x=140,y=380,width=200)

        regbutton=Button(self.root,text="Delete",font=("consolas",15,"bold"),command=self.mDelete,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=480,y=370,width=120,height=35)
        regbutton=Button(self.root,text="update",font=("consolas",15,"bold"),command=self.cursor,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=620,y=370,width=120,height=35)
    def fetch_data(self):
             #selected_item = self.cust_details_table.selection()[0]
        # print(self.cust_details_table.item(selected_item)['values'])
            #  cid = self.cust_details_table.item(selected_item)['values'][0]
            #  print(cid)
             conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
             my_cursor=conn.cursor()
             my_cursor.execute("select*from room_service")
             rows=my_cursor.fetchall()
             if len(rows)!=0:
                 self.cust_details_table.delete(*self.cust_details_table.get_children())
                 for i in rows:
                     
                     self.cust_details_table.insert("",END,values=i)
                    #  self.cust_details_table.insert(Button(text="del rec"),command=self.delete)
                    #  self.button6 = Button(self.cust_details_table, text="del rec", command=self.delete)  
                 conn.commit
             conn.close()
    def mDelete(self):
       
        selected_item = self.cust_details_table.selection()[0]
        # print(self.cust_details_table.item(selected_item)['values'])
        sid = self.cust_details_table.item(selected_item)['values'][0]
        
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            query = "DELETE FROM room_service WHERE ser_id =%s"
            value = (sid,)
            rs = my_cursor.execute(query,value)
           
            
            conn.commit()
            self.cust_details_table.delete(selected_item)
            conn.close()
            messagebox.showinfo("success","Data deleted successfully",parent=self.root)

            
        except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
    def showrs(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select * from room_service where rm_no LIKE '%{se.get()}%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
        conn.commit
        conn.close()

    def cursor(self):
        cursor_row=self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row,"values")
        print(content)
        #print(0,content[10])
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        con = content[0]
        my_cursor.execute("UPDATE room_service SET status='request accepted' WHERE ser_id="+content[0]
                                                    
                                                
                                                        

        )
        

        conn.commit()
        conn.close()
        
        messagebox.showinfo("sucess","Data updated successfully",parent=self.root)
        
        content[0].delete(0,END)
if __name__ == "__main__":
    root = Tk()
    app=rms_view(root)
    root.mainloop()