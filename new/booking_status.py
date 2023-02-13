from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
class bs_details:

    def __init__(self,root) :
       
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x570+225+205")

        global sel_roomno
        global des
        global sel_rmno
        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        frame1=Frame(self.root,bg="white",bd=10,relief=RAISED)
        frame1.place(x=250,y=180,width=600,height=200)

        lbl_title = Label(frame1,text="Check status",font=("times new roman",25,"bold"),bg="white",fg="grey",bd=5)
        lbl_title.place(x=220,y=20,width=200,height=30)

        floorno=Label(frame1,text="Roomno",font=("times new roman",10,"bold"),fg="black",bg="white")
        floorno.place(x=80,y=60)
        sel_rmno=StringVar()
        self.security_q=ttk.Combobox(frame1,font=("times new roman",10,"bold"),textvariable=sel_rmno,width=35)
        self.security_q["values"]=("select","101","102","103","104","105","106","201","202","203","204","205","206","301","302","303","304","305","306")
        self.security_q.place(x=200,y=60,width=230)
        self.security_q.current(0)
        # floorno=Label(frame1,text="Status",font=("times new roman",10,"bold"),fg="black",bg="white",relief=RIDGE,bd=5)
        # floorno.place(x=500,y=60,width=60)
        self.status=Label(frame1,text="",font=("times new roman",10,"bold"),fg="black",bg="white")
        self.status.place(x=260,y=145)
        regbutton=Button(frame1,text="check status",font=("times new roman",15,"bold"),command=self.sta,bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        regbutton.place(x=260,y=100,width=120,height=35)

    def sta(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute(f"select status from cust_booking where av_room LIKE '%{sel_rmno.get()}%'")
       
        rows=my_cursor.fetchone()
        if len(rows)!=0:
            if str(rows)!=('avialable',):

                self.status.config(text=f"Status-:{str(rows)}")
                self.status.after(200,self.sta)
                for i in rows:
                    self.status.insert("",END,values=i)
        conn.commit
        conn.close()
if __name__ == "__main__":
    root=Tk()
    obj1=bs_details(root)
    root.mainloop()