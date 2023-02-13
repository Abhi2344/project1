from logging import setLoggerClass
import re
from  tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import base64
import io
from tkinter import filedialog

conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class room_view:
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

        self.cust_details_table=ttk.Treeview(details_table,column=("rm_id","price","select_room","desc"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        selected_item = self.cust_details_table.selection()
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("rm_id",text="Room id")
        self.cust_details_table.heading("price",text="price")
        self.cust_details_table.heading("select_room",text="Room type")
        self.cust_details_table.heading("desc",text="description")
        
        
        
        
        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("rm_id",width=60)
        self.cust_details_table.column("price",width=60)
        self.cust_details_table.column("select_room",width=60)
        self.cust_details_table.column("desc",width=60)
        
        
        
        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

        regbutton=Button(self.root,text="search",font=("times new roman",15,"bold"),command=self.showrm,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        regbutton.place(x=10,y=370,width=120,height=35)

        se=StringVar()
        self.flno=ttk.Entry(self.root,font=("times new roman",10,"bold"),textvariable=se)
        self.flno.place(x=140,y=380,width=200)
        regbutton=Button(self.root,text="Delete",font=("times new roman",15,"bold"),command=self.mDelete,bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        regbutton.place(x=480,y=370,width=120,height=35)
    def fetch_data(self):
             #selected_item = self.cust_details_table.selection()[0]
        # print(self.cust_details_table.item(selected_item)['values'])
            #  cid = self.cust_details_table.item(selected_item)['values'][0]
            #  print(cid)
             conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
             my_cursor=conn.cursor()
             my_cursor.execute("select*from room_details")
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
            query = "DELETE FROM room_details WHERE rm_id =%s"
            value = (sid,)
            rs = my_cursor.execute(query,value)
           
            
            conn.commit()
            self.cust_details_table.delete(selected_item)
            conn.close()
            messagebox.showinfo("success","Data deleted successfully")

            
        except Exception as e  :
                        messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)

            #  image = ImageTk.PhotoImage(Image.open(self.cust_details_table))
            #  return image           
    # def delete(self):
    #         conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
    #         my_cursor=conn.cursor()
    #         id = int(self.my_cursor.get())
    #         my_cursor.execute("DELETE FROM room_details WHERE id=?", id)
    #         conn.commit()

    def showrm(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select * from room_details where select_room LIKE '%{se.get()}%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
        conn.commit
        conn.close()


if __name__ == "__main__":
    root = Tk()
    app=room_view(root)
    root.mainloop()

# from  tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox as msg
# import mysql.connector 
# import tkinter  as tk 


# my_conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
# my_w = tk.Tk()
# my_w.geometry("400x350") 
# def my_show():
#     r_set=my_conn.execute('''SELECT * from room_details''');
#     i=0 # row value inside the loop 
#     for student in r_set: 
#         for j in range(len(student)):
#             e = Entry(my_w, width=10, fg='blue') 
#             e.grid(row=i, column=j) 
#             e.insert(END, student[j])
#         e = Button(my_w, text='X',command=lambda d=student[0] : my_delete(d)) 
#         e.grid(row=i, column=j+1)
#         i=i+1
# def my_delete(id):
#     my_var=msg.askyesnocancel("Delete ?","Delete id:"+str(id),icon='warning',default='no')
#     if my_var: # True if yes button is clicked
#         r_set=my_conn.execute("DELETE FROM room_details WHERE id=" + str(id) );
#         msg.showerror("Deleted ","No of records deleted = " + str(r_set.rowcount))
#         my_conn.commit()
#         my_show() # refresh the window with new records
# my_show()  # open the window with record at the starting      
    
# my_w.mainloop()