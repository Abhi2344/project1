from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
from Room_details import rm_details
from Booking_detail import bok_details
import os
from dinin import dinin_details
from customer_details import cust_view
import mysql.connector
from tkinter.messagebox import showinfo
from tkinter import messagebox
import time as tm
from report import report
from Room_details import rm_details
from roominfo import room_view
conn = mysql.connector.connect(user="root", password="", host="localhost", database="hotel_management")
class sHotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")

        img1=Image.open("E:\hotel_images\hotel_images\hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        current_time=tm.strftime('%I:%M:%S')

        img2=Image.open("E:\hotel_images\hotel_images\logohotel.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=230,height=140)
        
        lbl_title = Label(self.root,text="Welcome ",font=("times new roman",25,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=140,width=1600,height=30)

        lbl_title1 = Label(lbl_title,text="Time-:"+current_time,font=("times new roman",15,"bold"),bg="black",fg="gold")
        lbl_title1.place(x=50,y=0,width=200,height=30)


        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=172,width=1550,height=620)

        lbl_menu = Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_menu.place(x=0,y=0,width=230)

        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=280)

        cust_btn=Button(btn_frame,text=" Din-in details      ",command=self.dinin1_details,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)


        cust_btn4=Button(btn_frame,text="  Booking details    ",command=self.bok1_details,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn4.grid(row=0,column=0,)

        # cust_btn1=Button(btn_frame,text="Add Room details      ",command=self.rm1_details,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        # cust_btn1.grid(row=2,column=0,pady=1)

        cust_btn2=Button(btn_frame,text="customer Details     ",command=self.view_cust,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn2.grid(row=2,column=0,pady=1)

        cust_btn2=Button(btn_frame,text="booking report     ",command=self.rep,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn2.grid(row=3,column=0,pady=1)
        cust_btn2=Button(btn_frame,text="Room Details     ",command=self.rmv,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn2.grid(row=5,column=0,pady=1)
        cust_btn2=Button(btn_frame,text="Add Room Details     ",command=self.rm1_details,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn2.grid(row=4,column=0,pady=1)

        # cust_btn2=Button(btn_frame,text="view Room details     ",command=self.rep,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        # cust_btn2.grid(row=5,column=0,pady=1)

        
        

        cust_btn4=Button(btn_frame,text="Logout     ",command=self.logout,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn4.grid(row=6,column=0,pady=1)
        
        # img3=Image.open("images\hotel1.png")
        # img3=img3.resize((1310,590),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img3)
        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=235,y=175,width=1400,height=650)

        self.label=Label(self.root,text="DASHBOARD",font=("times new roman",20),bg="orange")
        self.label.place(x=650,y=200,width=200)
        self.lbl_course=Label(self.root,text="Total customers \n[ 0 ]",font=("times new roman",20),bd=10,relief=RIDGE,bg="red",fg="white")
        self.lbl_course.place(x=480,y=300,width=250,height=200)
        self.lbl_room=Label(self.root,text="Total Rooms booked\n[ 0 ]",font=("times new roman",20),bd=10,relief=RIDGE,bg="blue",fg="white")
        self.lbl_room.place(x=800,y=300,width=250,height=200)
        # self.lbl_room=Label(self.root,text="Total Rooms avialable\n[ 0 ]",font=("times new roman",20),bd=10,relief=RIDGE,bg="blue",fg="white")
        # self.lbl_room.place(x=910,y=300,width=270,height=200)
        # lblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        # lblimg3.place(x=225,y=0,width=1310,height=450)


        img4=Image.open("E:\hotel_images\hotel_images\hotel3.jpg")
        img4=img4.resize((230,240),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=303,width=230,height=200)

        img5=Image.open("E:\hotel_images\hotel_images\hotel4.jpg")
        img5=img5.resize((230,240),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=480,width=230,height=240)
        self.dash()
        self.roomdash()
        
    def rm1_details(self):
        self.new_window=Toplevel(self.root)
        self.app=rm_details(self.new_window)
       
    def bok1_details(self):
        self.new_window=Toplevel(self.root)
        self.app=bok_details(self.new_window)
    def rep(self):
        self.new_window=Toplevel(self.root)
        self.app=report(self.new_window)

    def rmv(self):
        self.new_window=Toplevel(self.root)
        self.app=room_view(self.new_window)
    

    def dinin1_details(self):
        self.new_window=Toplevel(self.root)
        self.app=dinin_details(self.new_window)

    
    def view_cust(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_view(self.new_window)

    def logout(self):
        op=messagebox.askyesno("confirm","do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python staff_login.py")
    def dash(self):
        
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from cust_reg")
            cr=my_cursor.fetchall()
            self.lbl_course.config(text=f"Total customers \n[{str(len(cr))}]")
            self.lbl_course.after(200,self.dash)
          
        except Exception as e  :
                    messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)

    def roomdash(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from cust_booking where status='booking confirm'")
            cr=my_cursor.fetchall()
            self.lbl_room.config(text=f"Total rooms booked \n[{str(len(cr))}]")
            self.lbl_room.after(200,self.roomdash)
          
        except Exception as e  :
                    messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
    def roomdav(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from cust_booking where status='avialable'")
            cr=my_cursor.fetchall()
            self.lbl_room.config(text=f"Total Rooms avialable \n[{str(len(cr))}]")
            self.lbl_room.after(200,self.roomdav)
          
        except Exception as e  :
                    messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj= sHotelManagementSystem(root)
    root.mainloop()