from  tkinter import *
from tkinter import ttk
import mysql.connector
import os
from PIL import Image,ImageTk
from admin_home import HotelManagementSystem

from tkinter import messagebox





class login_window:
    # def validatepass():
    #     uname =username.get()
    #     passw = password.get()
    #     if uname=='' or passw=='':
    #         messagebox.showinfo("fill the empty field!!!")
    #     else:
    #         if uname=="admin" and passw=="admin":
    #          messagebox.showinfo("Login success")



    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")       

        
        global username
        global password
       
        self.bg=ImageTk.PhotoImage(file=r"E:\hotel_images\hotel_images\hotel1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black",bd=10,relief=RAISED)
        frame.place(x=510,y=170,width=340,height=450)

        img1=Image.open(r"E:\hotel_images\hotel_images\loginlogo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=635,y=175,width=100,height=100)

        get_str=Label(frame,text="Admin login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        username=lbl=Label(frame,text="User name",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

       
        username=StringVar()
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=username)
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)

        password=StringVar()
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=password,show="*")
        self.txtpass.place(x=40,y=260,width=270)

        img2=Image.open(r"E:\hotel_images\hotel_images\loginlogo.png")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=560,y=338,width=20,height=20)

        img3=Image.open(r"E:\hotel_images\hotel_images\password1.png")
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg2=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg2.place(x=560,y=413,width=20,height=20)


        loginbutton=Button(frame,text="login",command=self.admin_details,font=("times new roman",15,"bold"),bd=5,fg="gold",bg="blue",activeforeground="white",activebackground="red")
        loginbutton.place(x=110,y=300,width=120,height=35)


       
   
    


    def admin_details(self):
        uname =username.get()
        passw = password.get()
        if uname=='' or passw=='':
            messagebox.showwarning("Warning","All Fields are compulsory")
        else:
           if uname=="admin" and passw=="admin":
            messagebox.showinfo("Login success","You have logged in successfully")
            self.new_window=Toplevel(self.root)
            self.app=HotelManagementSystem(self.new_window)

           else:
                messagebox.showwarning("Warning","Enter valid username and password")

    







if __name__ == "__main__":
    root = Tk()
    app=login_window(root)
    root.mainloop()