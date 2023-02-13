from tkinter import*
from tkinter.font import BOLD
from PIL import Image, ImageTk
import os
from addstaff import sta_details
from staff_details import staff_view
import mysql.connector
from tkinter.messagebox import showinfo
from tkinter import messagebox
import time as tm
class HotelManagementSystem:
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
        
        lbl_title = Label(self.root,text="Welcome Admin",font=("times new roman",25,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=140,width=1600,height=30)
        lbl_title1 = Label(lbl_title,text="Time-:"+current_time,font=("times new roman",15,"bold"),bg="black",fg="gold")
        lbl_title1.place(x=50,y=0,width=200,height=30)

        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=172,width=1550,height=620)

        lbl_menu = Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_menu.place(x=0,y=0,width=230)

        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=240)

        cust_btn=Button(btn_frame,text=" view staff details     ",command=self.staff_view1,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)


        cust_btn4=Button(btn_frame,text="  Add staff    ",command=self.sta1_details,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn4.grid(row=0,column=0,)

        
        

        cust_btn4=Button(btn_frame,text="Logout     ",command=self.logout,width=22,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn4.grid(row=5,column=0,pady=1)
        
        # img3=Image.open("images\hotel1.png")
        # img3=img3.resize((1310,590),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # lblimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        # lblimg3.place(x=225,y=0,width=1310,height=450)
        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=235,y=175,width=1310,height=650)

        self.label=Label(self.root,text="DASHBOARD",font=("times new roman",20),bg="orange")
        self.label.place(x=650,y=200,width=200)
        self.lbl_course=Label(self.root,text="Total Receptionist \n[ 0 ]",font=("times new roman",20),bd=10,relief=RIDGE,bg="red",fg="white")
        self.lbl_course.place(x=350,y=300,width=250,height=200)
        self.lbl_kit=Label(self.root,text="Total Kitchen staff\n[ 0 ]",font=("times new roman",20),bd=10,relief=RIDGE,bg="blue",fg="white")
        self.lbl_kit.place(x=620,y=300,width=250,height=200)
        self.lbl_room=Label(self.root,text="Total Room staff\n[ 0 ]",font=("times new roman",20),bd=10,relief=RIDGE,bg="blue",fg="white")
        self.lbl_room.place(x=890,y=300,width=250,height=200)

        img4=Image.open("E:\hotel_images\hotel_images\hotel3.jpg")
        img4=img4.resize((230,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=0,y=150,width=230,height=250)

        img5=Image.open("E:\hotel_images\hotel_images\hotel4.jpg")
        img5=img5.resize((230,250),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=0,y=400,width=230,height=250)

        self.dashadmin()
        self.dashkt()
        self.dashrm()
    
    def sta1_details(self):
        self.new_window=Toplevel(self.root)
        self.app=sta_details(self.new_window)
    def staff_view1(self):
        self.new_window=Toplevel(self.root)
        self.app=staff_view(self.new_window)

    def dashadmin(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from staff_details where position='Recieptionist'")
            cr=my_cursor.fetchall()
            self.lbl_course.config(text=f"Total Receptionist \n[{str(len(cr))}]")
            self.lbl_course.after(200,self.dashadmin)
          
        except Exception as e  :
                    messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
    def logout(self):
        op=messagebox.askyesno("confirm","do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python admin_login.py")
    def dashkt(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from staff_details where position='Kitchen staff'")
            cr=my_cursor.fetchall()
            self.lbl_kit.config(text=f"Total Kitchen staff \n[{str(len(cr))}]")
            self.lbl_kit.after(200,self.dashkt)
          
        except Exception as e  :
                    messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)

    def dashrm(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="" ,database="hotel_management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from staff_details where position='Room service'")
            cr=my_cursor.fetchall()
            self.lbl_room.config(text=f"Total Room staff \n[{str(len(cr))}]")
            self.lbl_room.after(200,self.dashrm)
          
        except Exception as e  :
                    messagebox.showwarning("warning",f"Some thing went wrong:{str(e)}",parent=self.root)
    def logout(self):
        op=messagebox.askyesno("confirm","do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python sec.py")

if __name__ == "__main__":
    root = Tk()
    obj= HotelManagementSystem(root)
    root.mainloop()